# Security Policy

## Supported Versions

We actively support the latest version of this Stream Deck configuration:

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |

## Reporting a Vulnerability

If you discover a security vulnerability within this project, please send an email to Phillip Bock at [phillip.bock@lxd360.com](mailto:phillip.bock@lxd360.com). All security vulnerabilities will be promptly addressed.

Please do not open a public issue for security vulnerabilities.

### What to Include

When reporting a vulnerability, please include:

- A description of the vulnerability
- Steps to reproduce the issue
- Potential impact
- Any suggested fixes (if you have them)

## Security Considerations

This project consists primarily of:
- Configuration files (JSON)
- Documentation (Markdown, TXT, HTML)
- Python scripts for generating documentation

### Known Security Considerations

1. **VS Code Command IDs**: All command IDs in this configuration are standard VS Code commands. They are safe to use as they only execute built-in VS Code functionality.

2. **Python Scripts**: The Python scripts (`generate_streamdeck_config.py` and `quick_configurator.py`) are designed to:
   - Generate documentation files
   - Parse and validate JSON configuration
   - Create text-based outputs only
   - Not execute external commands
   - Not access network resources

3. **HTML Cheat Sheet**: The `streamdeck-cheatsheet.html` file is a static HTML document that:
   - Contains no JavaScript that executes on page load
   - Uses only inline styles (no external resources)
   - Is safe to open in any modern browser

### Best Practices for Users

When using this configuration:

1. **Verify Command IDs**: Before adding custom commands to your Stream Deck, verify they are legitimate VS Code command IDs through VS Code's Keyboard Shortcuts panel.

2. **Review Custom Configurations**: If you import custom configurations from other users, review the command IDs to ensure they are safe.

3. **Keep VS Code Updated**: Always use the latest version of VS Code to ensure you have the latest security patches.

4. **Extension Security**: The Stream Deck for VS Code extension (by Nicollas R.) is required. Install it from the official VS Code Marketplace.

## Responsible Disclosure

We appreciate responsible disclosure of any security issues. We will:

- Acknowledge your email within 48 hours
- Provide a more detailed response within 7 days
- Work with you to understand and resolve the issue
- Credit you in the release notes (if you wish)

Thank you for helping keep this project and its users safe!
