# _plugins/bibtex_reader.rb
# Parses _data/publications.bib and exposes entries as site.data['bib_pubs'].
# Each entry hash contains all parsed BibTeX fields plus:
#   'key'             => BibTeX cite key
#   'type'            => entry type (article, inproceedings, …)
#   'venue'           => journal / booktitle / school (whichever is present)
#   'authors_display' => human-readable "First Last, First Last" string
#   'raw'             => clean BibTeX snippet for the citation popup

module Jekyll
  class BibtexReader < Jekyll::Generator
    safe true
    priority :high

    UMLAUT = {
      'a' => 'ä', 'o' => 'ö', 'u' => 'ü', 'e' => 'ë', 'i' => 'ï',
      'A' => 'Ä', 'O' => 'Ö', 'U' => 'Ü', 'E' => 'Ë', 'I' => 'Ï'
    }.freeze

    ACUTE = {
      'a' => 'á', 'e' => 'é', 'o' => 'ó', 'u' => 'ú', 'i' => 'í',
      'A' => 'Á', 'E' => 'É', 'O' => 'Ó', 'U' => 'Ú', 'I' => 'Í'
    }.freeze

    GRAVE = {
      'a' => 'à', 'e' => 'è', 'i' => 'ì',
      'A' => 'À', 'E' => 'È', 'I' => 'Ì'
    }.freeze

    # Fields included in the popup raw BibTeX (custom fields excluded)
    STANDARD_ORDER = %w[
      title author journal booktitle volume number pages year
      publisher organization school address edition note
    ].freeze

    def generate(site)
      bib_path = File.join(site.source, '_data', 'publications.bib')
      return unless File.exist?(bib_path)

      site.data['bib_pubs'] = parse_bibtex(File.read(bib_path))
    end

    private

    # ── top-level parser ──────────────────────────────────────────────────────

    def parse_bibtex(content)
      entries = []
      pos = 0

      while (m = content.match(/@(\w+)\s*\{/i, pos))
        type = m[1].downcase

        # Walk forward from the opening '{' to find its matching '}'
        depth = 0
        j = m.end(0) - 1
        while j < content.length
          depth += 1 if content[j] == '{'
          if content[j] == '}'
            depth -= 1
            break if depth.zero?
          end
          j += 1
        end

        pos = j + 1
        next if %w[comment string preamble].include?(type)

        # Content between the outer braces
        inner = content[m.end(0)..j - 1]
        km    = inner.match(/\A\s*([^,\n]+)\s*,/)
        next unless km

        key    = km[1].strip
        fields = parse_fields(inner[km.end(0)..])
        raw    = build_raw_bib(type, key, fields)

        entry = {
          'key'             => key,
          'type'            => type,
          'raw'             => raw,
          'venue'           => fields['journal'] || fields['booktitle'] || fields['school'] || '',
          'authors_display' => format_authors(fields['author'] || '')
        }
        entries << entry.merge(fields)
      end

      entries
    end

    # ── field parser ─────────────────────────────────────────────────────────

    def parse_fields(body)
      fields = {}
      i = 0

      while i < body.length
        # skip whitespace / commas
        i += 1 while i < body.length && body[i] =~ /[\s,]/
        break if i >= body.length

        # read field name
        j = i
        j += 1 while j < body.length && body[j] =~ /\w/
        break if j == i

        name = body[i...j].downcase
        i    = j

        # skip whitespace / '='
        i += 1 while i < body.length && (body[i] =~ /\s/ || body[i] == '=')
        next unless i < body.length && body[i] == '{'

        # brace-balanced value extraction
        i     += 1          # skip opening '{'
        depth  = 1
        j      = i
        while j < body.length && depth > 0
          depth += 1 if body[j] == '{'
          depth -= 1 if body[j] == '}'
          j += 1
        end

        fields[name] = body[i...j - 1].strip
        i = j
      end

      fields
    end

    # ── raw BibTeX builder (standard fields only, no pdf/code/award/video) ───

    def build_raw_bib(type, key, fields)
      lines = ["@#{type}{#{key},"]
      STANDARD_ORDER.each do |f|
        next unless fields[f] && !fields[f].empty?
        lines << "  #{f} = {#{fields[f]}},"
      end
      lines[-1] = lines[-1].chomp(',') if lines.size > 1
      lines << '}'
      lines.join("\n")
    end

    # ── author formatting ─────────────────────────────────────────────────────

    def format_authors(raw)
      clean_latex(raw)
        .split(/\s+and\s+/)
        .map do |name|
          if name.include?(',')
            last, first = name.split(',', 2).map(&:strip)
            "#{first} #{last}"
          else
            name.strip
          end
        end
        .join(', ')
    end

    # ── LaTeX → Unicode ───────────────────────────────────────────────────────

    def clean_latex(text)
      text
        .gsub(/\{\\"([a-zA-Z])\}/)  { UMLAUT[$1] || $1 }
        .gsub(/\{\\'([a-zA-Z])\}/)  { ACUTE[$1]  || $1 }
        .gsub(/\{\\`([a-zA-Z])\}/)  { GRAVE[$1]  || $1 }
        .gsub(/\{\\~n\}/, 'ñ')
        .gsub(/\{\\c\{?c\}?\}/, 'ç')
        .gsub(/\{([^{}]*)\}/, '\1') # unwrap simple brace groups (two passes)
        .gsub(/\{([^{}]*)\}/, '\1')
        .tr('{}', '')               # remove any stray braces
    end
  end
end
