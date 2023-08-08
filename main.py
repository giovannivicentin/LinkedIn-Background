def colored_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def print_colored_box():
    box = f'''
{colored_text("                                                                                        ╔════════════════════════════════════════════════════╗", "0;30")}
{colored_text("                                                                                        ║", "0;30")}    {colored_text("              Giovanni Vicentin", "1;1")}    {colored_text("             ║", "0;30")}
{colored_text("                                                                                        ║", "0;30")} {colored_text("       Software Engineer | Full Stack Dev", "1;95")} {colored_text("         ║", "0;30")}
{colored_text("                                                                                        ║════════════════════════════════════════════════════║", "0;30")}
{colored_text("                                                                                        ║", "0;30")} {colored_text("Education: ", "0;34")} {colored_text("2 years Computer science College", "0;1")} {colored_text("      ║", "0;30")}
{colored_text("                                                                                        ║", "0;30")} {colored_text("Experience:", "0;34")} {colored_text("1 year Full Stack Dev", "0;1")} {colored_text("                 ║", "0;30")}
{colored_text("                                                                                        ║", "0;30")}                                      {colored_text("              ║", "0;30")}
{colored_text("                                                                                        ║", "0;30")} {colored_text("Technical Skills:", "0;34")}{colored_text(" - RPA         - Web Scraping  ", "0;1")} {colored_text("  ║", "0;30")}
{colored_text("                                                                                        ║", "0;30")}                   - NestJS      - React            {colored_text("║", "0;30")}
{colored_text("                                                                                        ║", "0;30")}                   - TypeScript  - Python           {colored_text("║", "0;30")}
{colored_text("                                                                                        ║", "0;30")}                   - Web Scraping            {colored_text("       ║", "0;30")}
{colored_text("                                                                                        ╚════════════════════════════════════════════════════╝", "0;30")}
'''

    print(box)

print_colored_box()
