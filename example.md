# Simple Markdown Reader

This is a **simple** markdown reader that displays markdown files with *beautiful* colored output in the terminal.

## Features

- Syntax highlighting for various markdown elements
- **Bold text** support
- *Italic text* support
- `inline code` formatting
- Code blocks with syntax
- Lists (ordered and unordered)
- Headers at multiple levels
- Blockquotes
- Links

---

### Installation

Simply clone this repository and run the script:

```bash
python3 md_reader.py example.md
```

### Supported Markdown Elements

#### Headers

Headers from H1 to H6 are supported with different colors and styling.

#### Text Formatting

You can use:
- **Bold text** with `**text**` or `__text__`
- *Italic text* with `*text*` or `_text_`
- ~~Strikethrough~~ with `~~text~~`
- `Inline code` with backticks

#### Lists

Unordered lists:
* First item
* Second item
  * Nested item 1
  * Nested item 2
* Third item

Ordered lists:
1. First step
2. Second step
3. Third step

#### Blockquotes

> This is a blockquote. It can contain multiple lines
> and will be displayed with special formatting.

#### Code Blocks

```python
def hello_world():
    print("Hello, World!")
    return True
```

```javascript
function greet(name) {
    console.log(`Hello, ${name}!`);
}
```

#### Links

Check out the [GitHub Repository](https://github.com/bhrionn/Simple-MD-Reader) for more information.

Visit [Python.org](https://python.org) to learn more about Python.

---

## Usage

Run the markdown reader with:

```
python3 md_reader.py <file.md>
```

## License

This is a simple educational project.
