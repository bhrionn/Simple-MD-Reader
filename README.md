# Simple-MD-Reader

A lightweight command-line Markdown reader that displays Markdown files with beautiful colored output directly in your terminal.

## Features

- **Syntax Highlighting**: Various markdown elements are displayed with different colors
- **Headers**: H1-H6 with different colors and underlines
- **Text Formatting**: Bold, italic, strikethrough, and inline code
- **Code Blocks**: Syntax-highlighted code blocks with language labels
- **Lists**: Ordered and unordered lists with nested support
- **Blockquotes**: Specially formatted quotes with visual indicators
- **Links**: Clickable links with URL display
- **Horizontal Rules**: Visual separators
- **No Dependencies**: Uses only Python standard library with ANSI color codes

## Installation

No installation required! Just make sure you have Python 3.6+ installed.

```bash
git clone https://github.com/bhrionn/Simple-MD-Reader.git
cd Simple-MD-Reader
chmod +x md_reader.py
```

## Usage

Run the markdown reader with any markdown file:

```bash
python3 md_reader.py <file.md>
```

Or make it executable and run directly:

```bash
./md_reader.py <file.md>
```

### Examples

```bash
# Display the example markdown file
python3 md_reader.py example.md

# Display this README
python3 md_reader.py README.md

# Display any other markdown file
python3 md_reader.py /path/to/your/document.md
```

## Supported Markdown Elements

- **Headers** (`# H1` through `###### H6`)
- **Bold** (`**text**` or `__text__`)
- **Italic** (`*text*` or `_text*`)
- **Strikethrough** (`~~text~~`)
- **Inline Code** (`` `code` ``)
- **Code Blocks** (``` ``` ```)
- **Unordered Lists** (`-`, `*`, or `+`)
- **Ordered Lists** (`1.`, `2.`, etc.)
- **Blockquotes** (`> quote`)
- **Links** (`[text](url)`)
- **Horizontal Rules** (`---`, `***`, or `___`)

## Color Scheme

The reader uses ANSI color codes to provide a visually appealing output:

- **H1 Headers**: Bright Magenta with double underline
- **H2 Headers**: Bright Cyan with underline
- **H3 Headers**: Bright Blue
- **H4-H6 Headers**: Various colors
- **Code Blocks**: Gray background with white text
- **Lists**: Yellow bullets
- **Blockquotes**: Cyan italic text with vertical bar
- **Links**: Bright blue underlined text with dimmed URLs
- **Inline Code**: Gray background

## Requirements

- Python 3.6 or higher
- Terminal with ANSI color support (most modern terminals)

## License

This is a simple educational project, free to use and modify.