import re

with open(r'd:\www\Notes\dice\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update tailwind config to add darkMode: 'class'
html = html.replace('theme: {', "darkMode: 'class',\n        theme: {")

# 2. Update body classes and remove custom body css
html = html.replace('<body class="antialiased min-h-screen">', '<body class="antialiased min-h-screen bg-[#f5f7fb] text-slate-800 dark:bg-slate-900 dark:text-slate-200 transition-colors duration-300">')
html = re.sub(r'body\s*\{\s*background-color:\s*#f5f7fb;\s*color:\s*#1e293b;\s*\}', '', html)

# 3. Add dark mode to dice faces
dice_css_old = """.dice-face-3d {
            position: absolute;
            width: 120px;
            height: 120px;
            background: white;
            border: 2px solid #4f46e5;"""
dice_css_new = """.dice-face-3d {
            position: absolute;
            width: 120px;
            height: 120px;
            background: white;
            border: 2px solid #4f46e5;
        }
        .dark .dice-face-3d {
            background: #1e293b;
        }
        .dice-face-3d {""" # re-open it to match original structure
html = html.replace(dice_css_old, dice_css_old.replace("background: white;", "background: white;\n        }\n        .dark .dice-face-3d {\n            background: #1e293b;\n        }\n        .dice-face-3d {\n            background: white;"))

# 4. Add dark: classes to elements
class_replacements = {
    'bg-white': 'bg-white dark:bg-slate-800 transition-colors duration-300',
    'border-slate-200': 'border-slate-200 dark:border-slate-700',
    'border-slate-100': 'border-slate-100 dark:border-slate-700/50',
    'text-slate-900': 'text-slate-900 dark:text-white',
    'text-slate-800': 'text-slate-800 dark:text-slate-100',
    'text-slate-600': 'text-slate-600 dark:text-slate-300',
    'text-slate-500': 'text-slate-500 dark:text-slate-400',
    'text-slate-400': 'text-slate-400 dark:text-slate-500',
    'bg-slate-100': 'bg-slate-100 dark:bg-slate-700/50',
}

for old_cls, new_cls in class_replacements.items():
    html = html.replace(old_cls, new_cls)

# 5. Add toggle button
toggle_button_html = """
    <!-- Dark Mode Toggle -->
    <div class="absolute top-4 right-4 z-50">
        <button id="theme-toggle" class="p-2 rounded-full bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 shadow-sm text-slate-500 dark:text-slate-400 hover:text-primary dark:hover:text-primary transition-colors duration-300">
            <svg id="theme-toggle-dark-icon" class="hidden w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z"></path></svg>
            <svg id="theme-toggle-light-icon" class="hidden w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0zm-.464 4.95l.707.707a1 1 0 001.414-1.414l-.707-.707a1 1 0 00-1.414 1.414zm2.12-10.607a1 1 0 010 1.414l-.706.707a1 1 0 11-1.414-1.414l.707-.707a1 1 0 011.414 0zM17 11a1 1 0 100-2h-1a1 1 0 100 2h1zm-7 4a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zM5.05 6.464A1 1 0 106.465 5.05l-.708-.707a1 1 0 00-1.414 1.414l.707.707zm1.414 8.486l-.707.707a1 1 0 01-1.414-1.414l.707-.707a1 1 0 011.414 1.414zM4 11a1 1 0 100-2H3a1 1 0 000 2h1z" fill-rule="evenodd" clip-rule="evenodd"></path></svg>
        </button>
    </div>

    <!-- Header -->"""
html = html.replace('<!-- Header -->', toggle_button_html)

# 6. Add toggle script
toggle_script = """
<script>
    var themeToggleDarkIcon = document.getElementById('theme-toggle-dark-icon');
    var themeToggleLightIcon = document.getElementById('theme-toggle-light-icon');

    if (localStorage.getItem('color-theme') === 'dark' || (!('color-theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
        themeToggleLightIcon.classList.remove('hidden');
        document.documentElement.classList.add('dark');
    } else {
        themeToggleDarkIcon.classList.remove('hidden');
    }

    var themeToggleBtn = document.getElementById('theme-toggle');

    themeToggleBtn.addEventListener('click', function() {
        themeToggleDarkIcon.classList.toggle('hidden');
        themeToggleLightIcon.classList.toggle('hidden');

        if (localStorage.getItem('color-theme')) {
            if (localStorage.getItem('color-theme') === 'light') {
                document.documentElement.classList.add('dark');
                localStorage.setItem('color-theme', 'dark');
            } else {
                document.documentElement.classList.remove('dark');
                localStorage.setItem('color-theme', 'light');
            }
        } else {
            if (document.documentElement.classList.contains('dark')) {
                document.documentElement.classList.remove('dark');
                localStorage.setItem('color-theme', 'light');
            } else {
                document.documentElement.classList.add('dark');
                localStorage.setItem('color-theme', 'dark');
            }
        }
    });
</script>
<script>"""
html = html.replace('<script>', toggle_script, 1)

with open(r'd:\www\Notes\dice\index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Dark mode feature added successfully!")
