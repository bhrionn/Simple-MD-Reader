#!/usr/bin/env python3
"""
Simple Markdown Reader with colored terminal output.
Displays markdown files with syntax highlighting and formatting.
"""

import sys
import re
import os
from typing import List, Tuple


class Colors:
    """ANSI color codes for terminal output."""
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    
    # Foreground colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    
    # Bright foreground colors
    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'
    
    # Background colors
    BG_BLACK = '\033[40m'
    BG_GRAY = '\033[100m'


class MarkdownRenderer:
    """Renders markdown text with colored terminal output."""
    
    def __init__(self):
        self.in_code_block = False
        self.code_block_lang = ""
    
    def render(self, markdown_text: str) -> str:
        """Render markdown text to colored terminal output."""
        lines = markdown_text.split('\n')
        output_lines = []
        
        for line in lines:
            rendered_line = self._render_line(line)
            output_lines.append(rendered_line)
        
        return '\n'.join(output_lines)
    
    def _render_line(self, line: str) -> str:
        """Render a single line of markdown."""
        # Handle code blocks
        if line.strip().startswith('```'):
            self.in_code_block = not self.in_code_block
            if self.in_code_block:
                self.code_block_lang = line.strip()[3:].strip()
                return f"{Colors.BG_GRAY}{Colors.BRIGHT_BLACK}╭─── {self.code_block_lang or 'code'} ───{Colors.RESET}"
            else:
                self.code_block_lang = ""
                return f"{Colors.BG_GRAY}{Colors.BRIGHT_BLACK}╰{'─' * 20}{Colors.RESET}"
        
        if self.in_code_block:
            return f"{Colors.BG_GRAY}{Colors.BRIGHT_WHITE}{line}{Colors.RESET}"
        
        # Handle headers
        if line.strip().startswith('#'):
            return self._render_header(line)
        
        # Handle horizontal rules
        if re.match(r'^\s*[-*_]{3,}\s*$', line):
            return f"{Colors.BRIGHT_BLACK}{'─' * 80}{Colors.RESET}"
        
        # Handle lists
        if re.match(r'^\s*[-*+]\s', line) or re.match(r'^\s*\d+\.\s', line):
            return self._render_list(line)
        
        # Handle blockquotes
        if line.strip().startswith('>'):
            return self._render_blockquote(line)
        
        # Handle inline formatting
        line = self._render_inline_formatting(line)
        
        return line
    
    def _render_header(self, line: str) -> str:
        """Render markdown headers."""
        match = re.match(r'^(#{1,6})\s+(.+)$', line.strip())
        if not match:
            return line
        
        level = len(match.group(1))
        text = match.group(2)
        
        # Store the original text length before formatting
        # Remove markdown formatting for length calculation
        clean_text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)
        clean_text = re.sub(r'__([^_]+)__', r'\1', clean_text)
        clean_text = re.sub(r'\*([^*]+)\*', r'\1', clean_text)
        clean_text = re.sub(r'_([^_]+)_', r'\1', clean_text)
        clean_text = re.sub(r'`([^`]+)`', r'\1', clean_text)
        clean_text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', clean_text)
        clean_text = re.sub(r'~~([^~]+)~~', r'\1', clean_text)
        visible_length = len(clean_text)
        
        # Apply inline formatting for display
        text = self._render_inline_formatting(text)
        
        colors = {
            1: (Colors.BOLD + Colors.BRIGHT_MAGENTA, '═'),
            2: (Colors.BOLD + Colors.BRIGHT_CYAN, '─'),
            3: (Colors.BOLD + Colors.BRIGHT_BLUE, '─'),
            4: (Colors.BOLD + Colors.BRIGHT_GREEN, ''),
            5: (Colors.BOLD + Colors.YELLOW, ''),
            6: (Colors.BOLD + Colors.WHITE, ''),
        }
        
        color, underline_char = colors.get(level, (Colors.BOLD, ''))
        
        result = f"\n{color}{text}{Colors.RESET}"
        if underline_char and level <= 2:
            result += f"\n{color}{underline_char * visible_length}{Colors.RESET}"
        
        return result
    
    def _render_list(self, line: str) -> str:
        """Render markdown lists."""
        # Detect list type and indentation
        match = re.match(r'^(\s*)([-*+]|\d+\.)\s+(.+)$', line)
        if not match:
            return line
        
        indent = match.group(1)
        marker = match.group(2)
        content = match.group(3)
        
        # Apply inline formatting to content
        content = self._render_inline_formatting(content)
        
        # Use different bullets for different indent levels
        if marker in ['-', '*', '+']:
            bullets = ['•', '◦', '▪', '▫']
            indent_level = len(indent) // 2
            bullet = bullets[min(indent_level, len(bullets) - 1)]
            return f"{indent}{Colors.BRIGHT_YELLOW}{bullet}{Colors.RESET} {content}"
        else:
            # Numbered list
            return f"{indent}{Colors.BRIGHT_YELLOW}{marker}{Colors.RESET} {content}"
    
    def _render_blockquote(self, line: str) -> str:
        """Render markdown blockquotes."""
        # Remove the > prefix and render content
        content = re.sub(r'^\s*>\s?', '', line)
        content = self._render_inline_formatting(content)
        return f"{Colors.BRIGHT_BLACK}▌{Colors.RESET} {Colors.ITALIC}{Colors.CYAN}{content}{Colors.RESET}"
    
    def _render_inline_formatting(self, text: str) -> str:
        """Render inline markdown formatting (bold, italic, code, links)."""
        # Inline code (process first to avoid conflicts)
        text = re.sub(
            r'`([^`]+)`',
            f'{Colors.BG_GRAY}{Colors.BRIGHT_WHITE}\\1{Colors.RESET}',
            text
        )
        
        # Bold and italic combined with *** (process before bold and italic separately)
        text = re.sub(
            r'\*\*\*([^*\n]+?)\*\*\*',
            f'{Colors.BOLD}{Colors.ITALIC}\\1{Colors.RESET}',
            text
        )
        
        # Bold with ** (process before single * for italic)
        text = re.sub(
            r'\*\*([^*\n]+?)\*\*',
            f'{Colors.BOLD}\\1{Colors.RESET}',
            text
        )
        # Bold with __
        text = re.sub(
            r'__([^_\n]+?)__',
            f'{Colors.BOLD}\\1{Colors.RESET}',
            text
        )
        
        # Italic with * (after bold **)
        text = re.sub(
            r'(?<!\*)\*([^*\n]+?)\*(?!\*)',
            f'{Colors.ITALIC}\\1{Colors.RESET}',
            text
        )
        # Italic with _
        text = re.sub(
            r'(?<!_)_([^_\n]+?)_(?!_)',
            f'{Colors.ITALIC}\\1{Colors.RESET}',
            text
        )
        
        # Links [text](url)
        text = re.sub(
            r'\[([^\]]+)\]\(([^)]+)\)',
            f'{Colors.UNDERLINE}{Colors.BRIGHT_BLUE}\\1{Colors.RESET} {Colors.DIM}{Colors.BRIGHT_BLACK}(\\2){Colors.RESET}',
            text
        )
        
        # Strikethrough
        text = re.sub(
            r'~~([^~]+)~~',
            f'{Colors.DIM}\\1{Colors.RESET}',
            text
        )
        
        return text


def read_markdown_file(filepath: str) -> str:
    """Read markdown file from disk."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"{Colors.BRIGHT_RED}Error: File '{filepath}' not found.{Colors.RESET}", file=sys.stderr)
        sys.exit(1)
    except IOError as e:
        print(f"{Colors.BRIGHT_RED}Error reading file: {e}{Colors.RESET}", file=sys.stderr)
        sys.exit(1)


def main():
    """Main entry point for the markdown reader."""
    if len(sys.argv) < 2:
        print(f"{Colors.BRIGHT_YELLOW}Usage: {sys.argv[0]} <markdown_file>{Colors.RESET}")
        print(f"\nExample: {sys.argv[0]} README.md")
        sys.exit(1)
    
    filepath = sys.argv[1]
    
    # Check if file exists
    if not os.path.exists(filepath):
        print(f"{Colors.BRIGHT_RED}Error: File '{filepath}' does not exist.{Colors.RESET}", file=sys.stderr)
        sys.exit(1)
    
    # Read and render the markdown file
    markdown_content = read_markdown_file(filepath)
    renderer = MarkdownRenderer()
    rendered_output = renderer.render(markdown_content)
    
    print(rendered_output)


if __name__ == '__main__':
    main()
