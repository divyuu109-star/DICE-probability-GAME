import re
import json

with open(r'd:\www\Notes\dice\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Tailwind colors
colors = {
    "surface-variant": "#636B2F",
    "on-background": "#D4DE95",
    "inverse-surface": "#BAC095",
    "tertiary": "#BAC095",
    "surface-bright": "#636B2F",
    "tertiary-fixed-dim": "#BAC095",
    "surface-container-lowest": "#3D4127",
    "on-surface-variant": "#D4DE95",
    "on-secondary-fixed-variant": "#D4DE95",
    "on-tertiary-container": "#D4DE95",
    "secondary-container": "#BAC095",
    "primary": "#D4DE95",
    "primary-fixed-dim": "#D4DE95",
    "surface-container-highest": "#636B2F",
    "on-tertiary-fixed": "#3D4127",
    "secondary-fixed-dim": "#BAC095",
    "surface": "#3D4127",
    "primary-fixed": "#D4DE95",
    "secondary-fixed": "#BAC095",
    "surface-dim": "#3D4127",
    "on-secondary-container": "#3D4127",
    "surface-tint": "#D4DE95",
    "on-tertiary": "#3D4127",
    "on-primary": "#3D4127",
    "on-primary-fixed": "#3D4127",
    "secondary": "#BAC095",
    "primary-container": "#BAC095",
    "outline": "#BAC095",
    "background": "#3D4127",
    "surface-container-low": "#636B2F",
    "surface-container": "#636B2F",
    "on-secondary": "#3D4127",
    "tertiary-fixed": "#BAC095",
    "on-secondary-fixed": "#3D4127",
    "inverse-on-surface": "#636B2F",
    "on-tertiary-fixed-variant": "#BAC095",
    "surface-container-high": "#636B2F",
    "on-surface": "#D4DE95",
    "outline-variant": "#BAC095",
    "on-primary-fixed-variant": "#BAC095",
    "inverse-primary": "#D4DE95",
    "tertiary-container": "#BAC095",
    "on-primary-container": "#3D4127",
}

# Use regex to replace color values in the tailwind config block
for name, color in colors.items():
    html = re.sub(rf'"{name}":\s*"#[a-fA-F0-9]+"!', f'"{name}": "{color}"', html)
    html = re.sub(rf'"{name}":\s*"#[a-fA-F0-9]+"', f'"{name}": "{color}"', html)

# Replace inline CSS background colors and rgbas
# Obsidian base #0f172a to #3D4127
html = html.replace('background-color: #0f172a;', 'background-color: #3D4127;')

# radial-gradient primary color (rgba(183, 109, 255, 0.1)) to rgba(212, 222, 149, 0.1)
html = html.replace('rgba(183, 109, 255, 0.1)', 'rgba(212, 222, 149, 0.1)')
html = html.replace('rgba(183, 109, 255, 0.05)', 'rgba(212, 222, 149, 0.05)')

# glass panel rgba(30, 41, 59, 0.4) to rgba(99, 107, 47, 0.4)
html = html.replace('rgba(30, 41, 59, 0.4)', 'rgba(99, 107, 47, 0.4)')

# old dice face
html = html.replace('rgba(15, 23, 42, 0.8)', 'rgba(61, 65, 39, 0.8)')
html = html.replace('rgba(76, 215, 246, 0.3)', 'rgba(186, 192, 149, 0.3)')
html = html.replace('rgba(76, 215, 246, 0.1)', 'rgba(186, 192, 149, 0.1)')

# new dice face
html = html.replace('rgba(15, 23, 42, 0.95)', 'rgba(61, 65, 39, 0.95)')
html = html.replace('2px solid #4cd7f6', '2px solid #BAC095')
html = html.replace('rgba(76, 215, 246, 0.2)', 'rgba(186, 192, 149, 0.2)')
html = html.replace('background-color: #4cd7f6', 'background-color: #BAC095')
html = html.replace('box-shadow: 0 0 8px #4cd7f6', 'box-shadow: 0 0 8px #BAC095')

# drop shadows in html classes
# shadow-[0_0_20px_rgba(3,181,211,0.15)]
html = html.replace('rgba(3,181,211,0.15)', 'rgba(186, 192, 149, 0.15)')
# shadow-[0_0_10px_rgba(221,183,255,0.5)]
html = html.replace('rgba(221,183,255,0.5)', 'rgba(212, 222, 149, 0.5)')
# shadow-[0_0_20px_rgba(221,183,255,0.4)]
html = html.replace('rgba(221,183,255,0.4)', 'rgba(212, 222, 149, 0.4)')
# hover:shadow-[0_0_30px_rgba(76,215,246,0.6)]
html = html.replace('rgba(76,215,246,0.6)', 'rgba(186, 192, 149, 0.6)')
# shadow-[0_-5px_25px_rgba(221,183,255,0.1)]
html = html.replace('rgba(221,183,255,0.1)', 'rgba(212, 222, 149, 0.1)')
# drop-shadow-[0_0_8px_rgba(221,183,255,0.6)]
html = html.replace('rgba(221,183,255,0.6)', 'rgba(212, 222, 149, 0.6)')

with open(r'd:\www\Notes\dice\index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Colors updated successfully in index.html!")
