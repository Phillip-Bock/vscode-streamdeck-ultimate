#!/usr/bin/env python3
"""
Stream Deck VS Code Configuration Generator
Converts configuration JSON into usable formats and documentation
"""

import json
from pathlib import Path
from typing import Dict, List, Any

class StreamDeckConfigGenerator:
    def __init__(self, config_path: str = "streamdeck-config-generator.json"):
        with open(config_path, 'r', encoding='utf-8') as f:
            self.config = json.load(f)
        self.layouts = self.config['streamdeck_layouts']
    
    def generate_markdown_guide(self) -> str:
        """Generate a comprehensive markdown reference guide"""
        md = ["# Stream Deck VS Code Configuration Guide\n"]
        md.append("## Quick Reference for All Pages\n")
        
        for page_id, page_data in self.layouts.items():
            page_name = page_data['name']
            buttons = page_data['buttons']
            
            md.append(f"### Page: {page_name}\n")
            md.append("| Position | Title | Command | Description |")
            md.append("|----------|-------|---------|-------------|")
            
            for btn in sorted(buttons, key=lambda x: (x['position'][0], x['position'][1])):
                row, col = btn['position']
                title = btn['title']
                command = btn['command']
                desc = btn['description']
                md.append(f"| Row {row+1}, Col {col+1} | {title} | `{command}` | {desc} |")
            
            md.append("")
        
        return "\n".join(md)
    
    def generate_setup_instructions(self) -> str:
        """Generate step-by-step setup instructions"""
        instructions = [
            "# Stream Deck Setup Instructions for VS Code\n",
            "## Prerequisites",
            "1. Stream Deck hardware (3x5 button layout)",
            "2. Stream Deck software installed",
            "3. VS Code with Stream Deck extension installed",
            "4. Extension: 'Stream Deck for Visual Studio Code' by Nicollas R.\n",
            "## Installation Steps\n",
            "### 1. Install VS Code Extension",
            "```bash",
            "# In VS Code, press Ctrl+P and paste:",
            "ext install nicollasr.vscode-streamdeck",
            "```\n",
            "### 2. Configure Stream Deck Plugin",
            "1. Open Stream Deck software",
            "2. Find 'Visual Studio Code' in the plugin list",
            "3. Drag 'Visual Studio Code: Execute Command' action to desired button",
            "4. Configure each button with the commands listed in the guide\n",
            "### 3. Getting Command IDs",
            "To add custom commands:",
            "1. In VS Code: File → Preferences → Keyboard Shortcuts",
            "2. Find your desired command",
            "3. Right-click → 'Copy Command ID'",
            "4. Paste this ID into Stream Deck button configuration\n",
            "### 4. Organize Your Pages",
            "Stream Deck software allows multiple pages:",
            "- Create a new page for each category (Navigation, Editing, Terminal, etc.)",
            "- Use the page navigation buttons to switch between pages",
            "- Consider adding a 'home' button on each page to return to your main page\n",
            "## Configuration Method\n"
        ]
        
        return "\n".join(instructions)
    
    def generate_csv_import(self) -> str:
        """Generate CSV for bulk importing button configurations"""
        csv = ["Page,Row,Col,Title,Command,Icon,Description"]
        
        for page_id, page_data in self.layouts.items():
            page_name = page_data['name']
            buttons = page_data['buttons']
            
            for btn in buttons:
                row, col = btn['position']
                title = btn['title'].replace(',', ';')
                command = btn['command']
                icon = btn.get('icon', '')
                desc = btn['description'].replace(',', ';')
                
                csv.append(f"{page_name},{row},{col},{title},{command},{icon},{desc}")
        
        return "\n".join(csv)
    
    def generate_command_list(self) -> str:
        """Generate a simple list of all commands for quick copying"""
        commands = ["# Complete Command List for VS Code Stream Deck\n"]
        commands.append("## All Available Commands\n")
        
        all_commands = set()
        for page_data in self.layouts.values():
            for btn in page_data['buttons']:
                all_commands.add((btn['command'], btn['title'], btn['description']))
        
        for cmd, title, desc in sorted(all_commands):
            commands.append(f"- **{title}**: `{cmd}` - {desc}")
        
        return "\n".join(commands)
    
    def generate_page_layout_visual(self) -> str:
        """Generate a visual representation of each page layout"""
        visual = ["# Stream Deck Visual Layout Guide\n"]
        visual.append("Each page is organized as 3 rows × 5 columns:\n")
        
        for page_id, page_data in self.layouts.items():
            page_name = page_data['name']
            buttons = page_data['buttons']
            
            # Create a 3x5 grid
            grid = [[None for _ in range(5)] for _ in range(3)]
            
            for btn in buttons:
                row, col = btn['position']
                grid[row][col] = btn
            
            visual.append(f"## {page_name}\n")
            visual.append("```")
            
            for row_idx, row in enumerate(grid):
                row_items = []
                for col_idx, btn in enumerate(row):
                    if btn:
                        # Truncate title to fit
                        title = btn['title'][:12]
                        icon = btn.get('icon', '')
                        row_items.append(f"{icon:2} {title:12}")
                    else:
                        row_items.append(" " * 15)
                visual.append(" | ".join(row_items))
                
                if row_idx < 2:
                    visual.append("-" * 85)
            
            visual.append("```\n")
        
        return "\n".join(visual)
    
    def generate_custom_template(self) -> Dict[str, Any]:
        """Generate a template for users to add their own custom page"""
        template = {
            "page_custom": {
                "name": "Your Custom Page",
                "buttons": [
                    {
                        "position": [row, col],
                        "title": f"Button {row}-{col}",
                        "command": "your.command.here",
                        "icon": "💡",
                        "description": "Your description here"
                    }
                    for row in range(3)
                    for col in range(5)
                ]
            }
        }
        return template
    
    def generate_all_outputs(self, output_dir: str = "/home/claude"):
        """Generate all output files"""
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        # Markdown reference guide
        with open(output_path / "streamdeck-reference-guide.md", 'w', encoding='utf-8') as f:
            f.write(self.generate_markdown_guide())
        
        # Setup instructions
        with open(output_path / "streamdeck-setup-instructions.md", 'w', encoding='utf-8') as f:
            f.write(self.generate_setup_instructions())
        
        # CSV import file
        with open(output_path / "streamdeck-import.csv", 'w', encoding='utf-8') as f:
            f.write(self.generate_csv_import())
        
        # Command list
        with open(output_path / "streamdeck-commands-list.md", 'w', encoding='utf-8') as f:
            f.write(self.generate_command_list())
        
        # Visual layout
        with open(output_path / "streamdeck-visual-layout.md", 'w', encoding='utf-8') as f:
            f.write(self.generate_page_layout_visual())
        
        # Custom template
        with open(output_path / "streamdeck-custom-template.json", 'w', encoding='utf-8') as f:
            json.dump(self.generate_custom_template(), f, indent=2)
        
        print("✅ Generated all Stream Deck configuration files:")
        print(f"  📄 streamdeck-reference-guide.md - Complete command reference")
        print(f"  📄 streamdeck-setup-instructions.md - Setup guide")
        print(f"  📄 streamdeck-import.csv - CSV for importing")
        print(f"  📄 streamdeck-commands-list.md - All commands list")
        print(f"  📄 streamdeck-visual-layout.md - Visual page layouts")
        print(f"  📄 streamdeck-custom-template.json - Template for custom pages")


if __name__ == "__main__":
    generator = StreamDeckConfigGenerator()
    generator.generate_all_outputs()
    print("\n✨ All files generated successfully in /home/claude/")
