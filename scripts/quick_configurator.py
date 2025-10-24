#!/usr/bin/env python3
"""
Quick Stream Deck Button Configurator
Interactive tool to help configure multiple buttons at once
"""

import json
from pathlib import Path

class QuickConfigurator:
    def __init__(self):
        self.config_file = Path("/home/claude/streamdeck-config-generator.json")
        with open(self.config_file, 'r') as f:
            self.config = json.load(f)
    
    def list_all_pages(self):
        """Display all available pages"""
        print("\n📱 Available Stream Deck Pages:\n")
        for idx, (page_id, page_data) in enumerate(self.config['streamdeck_layouts'].items(), 1):
            button_count = len(page_data['buttons'])
            print(f"{idx}. {page_data['name']} ({button_count} buttons)")
        print()
    
    def export_page_for_streamdeck(self, page_name: str) -> str:
        """Export a page in a format easy to use with Stream Deck software"""
        for page_id, page_data in self.config['streamdeck_layouts'].items():
            if page_data['name'].lower() == page_name.lower():
                buttons = page_data['buttons']
                
                output = [f"\n{'='*60}"]
                output.append(f"STREAM DECK CONFIGURATION: {page_data['name']}")
                output.append(f"{'='*60}\n")
                output.append("HOW TO USE THIS CONFIGURATION:")
                output.append("1. Open Stream Deck software")
                output.append("2. Create a new page (or use existing)")
                output.append("3. For each button below:")
                output.append("   - Drag 'Visual Studio Code: Execute Command' to button position")
                output.append("   - Set the title and command ID as specified")
                output.append("   - Optionally customize the icon\n")
                output.append(f"{'='*60}\n")
                
                for btn in sorted(buttons, key=lambda x: (x['position'][0], x['position'][1])):
                    row, col = btn['position']
                    output.append(f"📍 Position: Row {row+1}, Column {col+1}")
                    output.append(f"   Title: {btn['title']}")
                    output.append(f"   Command ID: {btn['command']}")
                    output.append(f"   Icon: {btn.get('icon', '📝')}")
                    output.append(f"   Description: {btn['description']}")
                    output.append(f"   {'-'*56}")
                
                return "\n".join(output)
        
        return f"❌ Page '{page_name}' not found!"
    
    def generate_streamdeck_profile(self):
        """Generate a text file that can be used as a reference when setting up Stream Deck"""
        output = ["STREAM DECK PROFILE SETUP GUIDE FOR VS CODE"]
        output.append("=" * 70)
        output.append("\nThis guide helps you set up all pages on your Stream Deck.\n")
        
        for page_id, page_data in self.config['streamdeck_layouts'].items():
            output.append("\n" + "=" * 70)
            output.append(f"PAGE: {page_data['name']}")
            output.append("=" * 70 + "\n")
            
            # Create visual grid
            grid = [[None for _ in range(5)] for _ in range(3)]
            for btn in page_data['buttons']:
                row, col = btn['position']
                grid[row][col] = btn
            
            # Print grid with button info
            for row_idx, row in enumerate(grid):
                output.append(f"\nRow {row_idx + 1}:")
                output.append("-" * 70)
                for col_idx, btn in enumerate(row):
                    if btn:
                        output.append(f"  [{col_idx + 1}] {btn['icon']} {btn['title']}")
                        output.append(f"      Command: {btn['command']}")
                        output.append(f"      Info: {btn['description']}")
                    else:
                        output.append(f"  [{col_idx + 1}] (empty)")
                    output.append("")
        
        return "\n".join(output)
    
    def create_page_by_page_instructions(self):
        """Create detailed page-by-page setup instructions"""
        instructions = []
        
        for idx, (page_id, page_data) in enumerate(self.config['streamdeck_layouts'].items(), 1):
            instructions.append(f"\n{'#'*70}")
            instructions.append(f"# STEP {idx}: Setting up '{page_data['name']}' Page")
            instructions.append(f"{'#'*70}\n")
            
            instructions.append("1. In Stream Deck software, create a new page or select existing")
            instructions.append(f"2. Name the page: '{page_data['name']}'")
            instructions.append("3. Configure each button as follows:\n")
            
            for btn in sorted(page_data['buttons'], key=lambda x: (x['position'][0], x['position'][1])):
                row, col = btn['position']
                instructions.append(f"   Button at Row {row+1}, Col {col+1}:")
                instructions.append(f"   ├─ Drag: 'Visual Studio Code: Execute Command'")
                instructions.append(f"   ├─ Title: {btn['title']}")
                instructions.append(f"   ├─ Command (ID): {btn['command']}")
                instructions.append(f"   ├─ Suggested Icon: {btn.get('icon', '📝')}")
                instructions.append(f"   └─ Purpose: {btn['description']}\n")
            
            instructions.append(f"✅ Page {idx} Complete! Test each button to ensure it works.\n")
        
        return "\n".join(instructions)


def main():
    configurator = QuickConfigurator()
    
    print("\n" + "="*70)
    print("🎛️  STREAM DECK VS CODE CONFIGURATION TOOL")
    print("="*70)
    print("\nGenerating setup files...\n")
    
    # Generate profile guide
    profile_text = configurator.generate_streamdeck_profile()
    with open("/home/claude/streamdeck-profile-guide.txt", 'w', encoding='utf-8') as f:
        f.write(profile_text)
    print("✅ Created: streamdeck-profile-guide.txt")
    
    # Generate page-by-page instructions
    instructions = configurator.create_page_by_page_instructions()
    with open("/home/claude/streamdeck-setup-step-by-step.txt", 'w', encoding='utf-8') as f:
        f.write(instructions)
    print("✅ Created: streamdeck-setup-step-by-step.txt")
    
    # Export individual page configurations
    for page_id, page_data in configurator.config['streamdeck_layouts'].items():
        page_name = page_data['name']
        page_export = configurator.export_page_for_streamdeck(page_name)
        
        safe_filename = page_name.lower().replace(' ', '-').replace('&', 'and')
        filename = f"/home/claude/page-{safe_filename}.txt"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(page_export)
        print(f"✅ Created: page-{safe_filename}.txt")
    
    print("\n" + "="*70)
    print("✨ All configuration files generated successfully!")
    print("="*70)
    print("\n📂 Files created in /home/claude/:")
    print("   • streamdeck-profile-guide.txt - Complete overview")
    print("   • streamdeck-setup-step-by-step.txt - Step-by-step setup")
    print("   • page-*.txt - Individual page configurations")
    print("\n💡 TIP: Start with 'streamdeck-setup-step-by-step.txt' for easiest setup!")
    print()


if __name__ == "__main__":
    main()
