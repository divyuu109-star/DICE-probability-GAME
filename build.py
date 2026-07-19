import re

with open(r'C:\Users\Divu\.gemini\antigravity-ide\brain\5791a122-464b-4aba-961c-5cf160d95ee2\.system_generated\steps\27\content.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract HTML content
html_match = re.search(r'<!DOCTYPE html>.*</html>', content, re.DOTALL)
html = html_match.group(0)

# Add custom CSS
custom_css = """
        /* 3D Dice styles */
        .dice-scene {
            width: 120px;
            height: 120px;
            perspective: 600px;
        }
        .dice-cube {
            width: 100%;
            height: 100%;
            position: relative;
            transform-style: preserve-3d;
            transform: translateZ(-60px) rotateX(-15deg) rotateY(15deg);
            transition: transform 1.5s ease-out; /* For rolling animation */
        }
        .dice-face-3d {
            position: absolute;
            width: 120px;
            height: 120px;
            background: rgba(15, 23, 42, 0.95);
            border: 2px solid #4cd7f6; /* theme('colors.secondary') */
            box-shadow: inset 0 0 15px rgba(76, 215, 246, 0.2);
            border-radius: 16px;
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            grid-template-rows: repeat(3, 1fr);
            gap: 8px;
            padding: 16px;
        }
        .dice-face-3d .pip-3d {
            background-color: #4cd7f6; /* theme('colors.secondary') */
            box-shadow: 0 0 8px #4cd7f6;
            border-radius: 50%;
            width: 100%;
            height: 100%;
            align-self: center;
            justify-self: center;
        }

        /* Face positioning */
        .dice-face-front  { transform: rotateY(  0deg) translateZ(60px); }
        .dice-face-back   { transform: rotateY(180deg) translateZ(60px); }
        .dice-face-right  { transform: rotateY( 90deg) translateZ(60px); }
        .dice-face-left   { transform: rotateY(-90deg) translateZ(60px); }
        .dice-face-top    { transform: rotateX( 90deg) translateZ(60px); }
        .dice-face-bottom { transform: rotateX(-90deg) translateZ(60px); }

        /* Pip placements */
        .face-1 .pip-3d:nth-child(1) { grid-area: 2 / 2 / 3 / 3; }
        
        .face-2 .pip-3d:nth-child(1) { grid-area: 1 / 1 / 2 / 2; }
        .face-2 .pip-3d:nth-child(2) { grid-area: 3 / 3 / 4 / 4; }
        
        .face-3 .pip-3d:nth-child(1) { grid-area: 1 / 1 / 2 / 2; }
        .face-3 .pip-3d:nth-child(2) { grid-area: 2 / 2 / 3 / 3; }
        .face-3 .pip-3d:nth-child(3) { grid-area: 3 / 3 / 4 / 4; }
        
        .face-4 .pip-3d:nth-child(1) { grid-area: 1 / 1 / 2 / 2; }
        .face-4 .pip-3d:nth-child(2) { grid-area: 1 / 3 / 2 / 4; }
        .face-4 .pip-3d:nth-child(3) { grid-area: 3 / 1 / 4 / 2; }
        .face-4 .pip-3d:nth-child(4) { grid-area: 3 / 3 / 4 / 4; }
        
        .face-5 .pip-3d:nth-child(1) { grid-area: 1 / 1 / 2 / 2; }
        .face-5 .pip-3d:nth-child(2) { grid-area: 1 / 3 / 2 / 4; }
        .face-5 .pip-3d:nth-child(3) { grid-area: 2 / 2 / 3 / 3; }
        .face-5 .pip-3d:nth-child(4) { grid-area: 3 / 1 / 4 / 2; }
        .face-5 .pip-3d:nth-child(5) { grid-area: 3 / 3 / 4 / 4; }
        
        .face-6 .pip-3d:nth-child(1) { grid-area: 1 / 1 / 2 / 2; }
        .face-6 .pip-3d:nth-child(2) { grid-area: 2 / 1 / 3 / 2; }
        .face-6 .pip-3d:nth-child(3) { grid-area: 3 / 1 / 4 / 2; }
        .face-6 .pip-3d:nth-child(4) { grid-area: 1 / 3 / 2 / 4; }
        .face-6 .pip-3d:nth-child(5) { grid-area: 2 / 3 / 3 / 4; }
        .face-6 .pip-3d:nth-child(6) { grid-area: 3 / 3 / 4 / 4; }
"""
html = html.replace('</style>', custom_css + '\n</style>')

# Replace dice placeholder
old_dice = '''<div class="w-[120px] h-[120px] relative mb-[32px] flex items-center justify-center" id="dice-3d-placeholder">
<!-- Static CSS representation of a dice face for the placeholder -->
<div class="w-full h-full rounded-[16px] dice-face flex items-center justify-center relative overflow-hidden">
<div class="absolute inset-0 bg-gradient-to-br from-white/5 to-transparent z-0"></div>
<div class="grid grid-cols-3 grid-rows-3 gap-[12px] p-[24px] w-full h-full z-10">
<div class="w-[16px] h-[16px] pip rounded-full place-self-center"></div>
<div></div>
<div class="w-[16px] h-[16px] pip rounded-full place-self-center"></div>
<div></div>
<div class="w-[16px] h-[16px] pip rounded-full place-self-center"></div>
<div></div>
<div class="w-[16px] h-[16px] pip rounded-full place-self-center"></div>
<div></div>
<div class="w-[16px] h-[16px] pip rounded-full place-self-center"></div>
</div>
</div>
</div>'''

new_dice = '''<div class="dice-scene mb-[32px]">
    <div class="dice-cube" id="dice-cube">
        <div class="dice-face-3d dice-face-front face-1"><div class="pip-3d"></div></div>
        <div class="dice-face-3d dice-face-back face-2"><div class="pip-3d"></div><div class="pip-3d"></div></div>
        <div class="dice-face-3d dice-face-right face-3"><div class="pip-3d"></div><div class="pip-3d"></div><div class="pip-3d"></div></div>
        <div class="dice-face-3d dice-face-left face-4"><div class="pip-3d"></div><div class="pip-3d"></div><div class="pip-3d"></div><div class="pip-3d"></div></div>
        <div class="dice-face-3d dice-face-top face-5"><div class="pip-3d"></div><div class="pip-3d"></div><div class="pip-3d"></div><div class="pip-3d"></div><div class="pip-3d"></div></div>
        <div class="dice-face-3d dice-face-bottom face-6"><div class="pip-3d"></div><div class="pip-3d"></div><div class="pip-3d"></div><div class="pip-3d"></div><div class="pip-3d"></div><div class="pip-3d"></div></div>
    </div>
</div>'''
html = html.replace(old_dice, new_dice)

# Update Feedback Area
html = html.replace('<div class="font-display-xl text-display-xl text-primary font-black">5</div>', '<div class="font-display-xl text-display-xl text-primary font-black" id="prediction-display">?</div>')
html = html.replace('<div class="font-body-md text-body-md text-on-background mt-[8px]">Waiting for roll...</div>', '<div class="font-body-md text-body-md text-on-background mt-[8px]" id="result-message">Waiting for roll...</div>')

# Update Stat Card 1
html = html.replace('<span class="font-stat-lg text-stat-lg text-on-background">0</span>', '<span class="font-stat-lg text-stat-lg text-on-background" id="stat-total-rolls">0</span>', 1)

# Update Stat Card 2
html = html.replace('<span class="font-stat-lg text-stat-lg text-secondary">0</span>', '<span class="font-stat-lg text-stat-lg text-secondary" id="stat-streak">0</span>', 1)

# Update Stat Card 3
html = html.replace('<span class="font-stat-lg text-stat-lg text-primary">0/0 (0%)</span>', '<span class="font-stat-lg text-stat-lg text-primary" id="stat-accuracy">0/0 (0%)</span>', 1)
html = html.replace('<div class="h-full w-0 bg-gradient-to-r from-primary to-secondary rounded-full shadow-[0_0_10px_rgba(221,183,255,0.5)]"></div>', '<div id="accuracy-bar" class="h-full w-0 bg-gradient-to-r from-primary to-secondary rounded-full shadow-[0_0_10px_rgba(221,183,255,0.5)] transition-all duration-300"></div>')

# Update Roll Frequency
for i in range(1, 7):
    old_row = f'''<div class="flex items-center gap-[12px]">
<div class="w-[24px] font-stat-lg text-stat-lg text-on-background text-center">{i}</div>
<div class="flex-grow h-[12px] bg-surface-variant rounded-full overflow-hidden">
<div class="h-full w-[0%] bg-tertiary-fixed-dim rounded-full"></div>
</div>
<div class="w-[32px] font-label-sm text-label-sm text-on-surface-variant text-right">0</div>
</div>'''
    
    new_row = f'''<div class="flex items-center gap-[12px]">
<div class="w-[24px] font-stat-lg text-stat-lg text-on-background text-center">{i}</div>
<div class="flex-grow h-[12px] bg-surface-variant rounded-full overflow-hidden">
<div id="bar-fill-{i}" class="h-full w-[0%] bg-tertiary-fixed-dim rounded-full transition-all duration-300"></div>
</div>
<div id="bar-val-{i}" class="w-[32px] font-label-sm text-label-sm text-on-surface-variant text-right">0</div>
</div>'''
    html = html.replace(old_row, new_row)

# Update button
html = html.replace('<button class="w-full max-w-[300px] bg-gradient-to-r', '<button id="roll-button" class="w-full max-w-[300px] bg-gradient-to-r')

# Add JS logic
js_logic = """
<script>
    let totalRolls = 0;
    let correctPredictions = 0;
    let currentStreak = 0;
    let faceFrequencies = { 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0 };
    let rollHistory = [];
    let isRolling = false;

    // AI logic: simulate learning from data
    // Random prediction for the first 5 rolls to gather data, 
    // then predicts the most frequent face.
    function predictNextRoll() {
        if (totalRolls < 5) {
            return Math.floor(Math.random() * 6) + 1;
        }
        
        let maxFreq = 0;
        let predictedFace = 1;
        for (let face = 1; face <= 6; face++) {
            if (faceFrequencies[face] > maxFreq) {
                maxFreq = faceFrequencies[face];
                predictedFace = face;
            } else if (faceFrequencies[face] === maxFreq) {
                if (Math.random() > 0.5) predictedFace = face;
            }
        }
        return predictedFace;
    }

    function updateStats(actualRoll, aiPrediction) {
        totalRolls++;
        faceFrequencies[actualRoll]++;
        rollHistory.push(actualRoll);

        let isCorrect = actualRoll === aiPrediction;
        const msgEl = document.getElementById('result-message');
        if (isCorrect) {
            correctPredictions++;
            currentStreak++;
            msgEl.innerText = "AI got it right! 🎉";
            msgEl.className = "font-body-md text-body-md text-primary mt-[8px]";
        } else {
            currentStreak = 0;
            msgEl.innerText = "AI missed this time.";
            msgEl.className = "font-body-md text-body-md text-error mt-[8px]";
        }

        let accuracy = ((correctPredictions / totalRolls) * 100).toFixed(1);
        
        // Update DOM stats
        document.getElementById('stat-total-rolls').innerText = totalRolls;
        document.getElementById('stat-streak').innerText = currentStreak;
        document.getElementById('stat-accuracy').innerText = `${correctPredictions}/${totalRolls} (${accuracy}%)`;
        document.getElementById('accuracy-bar').style.width = `${accuracy}%`;

        // Update charts
        for (let i = 1; i <= 6; i++) {
            let freq = faceFrequencies[i];
            let pct = totalRolls > 0 ? (freq / totalRolls) * 100 : 0;
            document.getElementById(`bar-val-${i}`).innerText = freq;
            document.getElementById(`bar-fill-${i}`).style.width = `${pct}%`;
            if (pct > 0) {
                document.getElementById(`bar-fill-${i}`).className = "h-full bg-gradient-to-r from-primary to-secondary rounded-full transition-all duration-300";
            }
        }
    }

    document.getElementById('roll-button').addEventListener('click', () => {
        if (isRolling) return;
        isRolling = true;
        
        let prediction = predictNextRoll();
        document.getElementById('prediction-display').innerText = prediction;
        document.getElementById('result-message').innerText = "Rolling...";
        document.getElementById('result-message').className = "font-body-md text-body-md text-on-background mt-[8px]";

        const cube = document.getElementById('dice-cube');
        cube.style.transition = 'none';
        cube.style.transform = 'translateZ(-60px) rotateX(0deg) rotateY(0deg) rotateZ(0deg)';
        
        // Trigger reflow
        void cube.offsetWidth;
        
        cube.style.transition = 'transform 1.5s ease-out';
        
        // Actual random roll
        const actualRoll = Math.floor(Math.random() * 6) + 1;
        
        // Random rotations to spin around before landing
        const spinX = Math.floor(Math.random() * 4) * 360 + 720;
        const spinY = Math.floor(Math.random() * 4) * 360 + 720;

        let finalRotateX = spinX;
        let finalRotateY = spinY;

        switch (actualRoll) {
            case 1: finalRotateX += 0; finalRotateY += 0; break;
            case 2: finalRotateX += 0; finalRotateY -= 180; break;
            case 3: finalRotateX += 0; finalRotateY -= 90; break;
            case 4: finalRotateX += 0; finalRotateY += 90; break;
            case 5: finalRotateX -= 90; finalRotateY += 0; break;
            case 6: finalRotateX += 90; finalRotateY += 0; break;
        }

        cube.style.transform = `translateZ(-60px) rotateX(${finalRotateX}deg) rotateY(${finalRotateY}deg)`;

        setTimeout(() => {
            updateStats(actualRoll, prediction);
            isRolling = false;
        }, 1500);
    });
</script>
</body>
"""

html = html.replace('</body>', js_logic)

import os
os.makedirs(r'd:\www\Notes\dice', exist_ok=True)
with open(r'd:\www\Notes\dice\index.html', 'w', encoding='utf-8') as f:
    f.write(html)
