import json

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8"/>
    <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
    <title>AI Dice Probability Game</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet"/>
    <script>
      tailwind.config = {
        theme: {
          extend: {
            fontFamily: {
              sans: ['Inter', 'sans-serif'],
            },
            colors: {
              primary: '#4f46e5',
              error: '#dc2626',
              'on-background': '#475569'
            }
          },
        },
      }
    </script>
    <style>
        body {
            background-color: #f5f7fb;
            color: #1e293b;
        }
        
        /* Overrides for JS-injected classes */
        .text-body-md { font-size: 0.875rem; }
        .bg-gradient-to-r.from-primary.to-secondary {
            background-image: none !important;
            background-color: #0ea5e9 !important;
        }

        /* 3D Dice styles */
        .dice-scene {
            width: 120px;
            height: 120px;
            perspective: 600px;
            margin: 0 auto 32px auto;
        }
        .dice-cube {
            width: 100%;
            height: 100%;
            position: relative;
            transform-style: preserve-3d;
            transform: translateZ(-60px) rotateX(-15deg) rotateY(15deg);
        }
        .dice-face-3d {
            position: absolute;
            width: 120px;
            height: 120px;
            background: white;
            border: 2px solid #4f46e5;
            border-radius: 16px;
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            grid-template-rows: repeat(3, 1fr);
            gap: 8px;
            padding: 16px;
        }
        .dice-face-3d .pip-3d {
            background-color: #4f46e5;
            border-radius: 50%;
            width: 100%;
            height: 100%;
            align-self: center;
            justify-self: center;
        }

        .dice-face-front  { transform: rotateY(  0deg) translateZ(60px); }
        .dice-face-back   { transform: rotateY(180deg) translateZ(60px); }
        .dice-face-right  { transform: rotateY( 90deg) translateZ(60px); }
        .dice-face-left   { transform: rotateY(-90deg) translateZ(60px); }
        .dice-face-top    { transform: rotateX( 90deg) translateZ(60px); }
        .dice-face-bottom { transform: rotateX(-90deg) translateZ(60px); }

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
    </style>
</head>
<body class="antialiased min-h-screen">

<main class="max-w-[560px] mx-auto px-4 py-12 flex flex-col">
    
    <!-- Header -->
    <div class="text-center mb-8">
        <h1 class="text-2xl font-bold text-slate-900 mb-1">AI Dice Probability Game</h1>
        <p class="text-sm text-slate-500">Demonstrating the intersection of AI prediction and mathematical randomness.</p>
    </div>

    <!-- Dice & Prediction Card -->
    <div class="bg-white border border-slate-200 shadow-sm rounded-[14px] p-8 mb-6 flex flex-col items-center">
        <!-- 3D Dice -->
        <div class="dice-scene">
            <div class="dice-cube" id="dice-cube">
                <div class="dice-face-3d dice-face-front face-1"><div class="pip-3d"></div></div>
                <div class="dice-face-3d dice-face-back face-2"><div class="pip-3d"></div><div class="pip-3d"></div></div>
                <div class="dice-face-3d dice-face-right face-3"><div class="pip-3d"></div><div class="pip-3d"></div><div class="pip-3d"></div></div>
                <div class="dice-face-3d dice-face-left face-4"><div class="pip-3d"></div><div class="pip-3d"></div><div class="pip-3d"></div><div class="pip-3d"></div></div>
                <div class="dice-face-3d dice-face-top face-5"><div class="pip-3d"></div><div class="pip-3d"></div><div class="pip-3d"></div><div class="pip-3d"></div><div class="pip-3d"></div></div>
                <div class="dice-face-3d dice-face-bottom face-6"><div class="pip-3d"></div><div class="pip-3d"></div><div class="pip-3d"></div><div class="pip-3d"></div><div class="pip-3d"></div><div class="pip-3d"></div></div>
            </div>
        </div>

        <!-- Prediction -->
        <div class="w-full text-center border-t border-slate-100 pt-6">
            <div class="text-xs font-semibold text-slate-400 uppercase tracking-wider">AI PREDICTS</div>
            <div class="text-4xl font-bold text-primary my-2" id="prediction-display">?</div>
            <div class="text-sm text-slate-500" id="result-message">Waiting for roll...</div>
        </div>
    </div>

    <!-- Roll Button -->
    <button id="roll-button" class="w-full bg-primary hover:bg-indigo-700 text-white font-semibold py-3.5 rounded-[12px] shadow-sm transition-colors mb-6 flex items-center justify-center gap-2">
        <span>Roll Dice</span>
    </button>

    <!-- Stats Dashboard -->
    <div class="grid grid-cols-2 gap-4 mb-6">
        <!-- Stat Card 1 -->
        <div class="bg-white border border-slate-200 shadow-sm rounded-[14px] p-5 flex flex-col">
            <span class="text-xs font-semibold text-slate-400 uppercase tracking-wider">Total Rolls</span>
            <span class="text-2xl font-bold text-slate-800 mt-1" id="stat-total-rolls">0</span>
        </div>
        
        <!-- Stat Card 2 -->
        <div class="bg-white border border-slate-200 shadow-sm rounded-[14px] p-5 flex flex-col">
            <span class="text-xs font-semibold text-slate-400 uppercase tracking-wider">Current Streak</span>
            <span class="text-2xl font-bold text-primary mt-1" id="stat-streak">0</span>
        </div>
        
        <!-- Stat Card 3 -->
        <div class="bg-white border border-slate-200 shadow-sm rounded-[14px] p-5 col-span-2 flex flex-col">
            <div class="flex justify-between items-center w-full mb-3">
                <span class="text-xs font-semibold text-slate-400 uppercase tracking-wider">AI Accuracy</span>
                <span class="text-lg font-bold text-primary" id="stat-accuracy">0/0 (0%)</span>
            </div>
            <div class="w-full h-2 bg-slate-100 rounded-full overflow-hidden">
                <div id="accuracy-bar" class="h-full w-0 bg-primary transition-all duration-300"></div>
            </div>
        </div>
    </div>

    <!-- Bar Chart -->
    <div class="bg-white border border-slate-200 shadow-sm rounded-[14px] p-6">
        <h3 class="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-5">Roll Frequency Distribution</h3>
        <div class="flex flex-col gap-3">
            <!-- Rows 1-6 -->
"""

for i in range(1, 7):
    html_content += f"""
            <div class="flex items-center gap-3">
                <div class="w-4 text-sm font-semibold text-slate-600 text-center">{i}</div>
                <div class="flex-grow h-2.5 bg-slate-100 rounded-full overflow-hidden">
                    <div id="bar-fill-{i}" class="h-full w-0 bg-[#0ea5e9] transition-all duration-300"></div>
                </div>
                <div id="bar-val-{i}" class="w-8 text-xs font-medium text-slate-500 text-right">0</div>
            </div>
"""

html_content += """
        </div>
    </div>

    <!-- Footnote -->
    <p class="text-center text-xs text-slate-400 mt-6">Theoretical probability for each face is 16.67% (1/6).</p>

</main>

<script>
    let totalRolls = 0;
    let correctPredictions = 0;
    let currentStreak = 0;
    let faceFrequencies = { 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0 };
    let rollHistory = [];
    let isRolling = false;

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
        
        document.getElementById('stat-total-rolls').innerText = totalRolls;
        document.getElementById('stat-streak').innerText = currentStreak;
        document.getElementById('stat-accuracy').innerText = `${correctPredictions}/${totalRolls} (${accuracy}%)`;
        document.getElementById('accuracy-bar').style.width = `${accuracy}%`;

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
        
        void cube.offsetWidth;
        
        cube.style.transition = 'transform 1.5s ease-out';
        
        const actualRoll = Math.floor(Math.random() * 6) + 1;
        
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
</html>
"""

with open(r'd:\www\Notes\dice\index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Redesigned index.html successfully!")
