<!DOCTYPE html>
<html lang="pt-PT">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Extrator Mágico de Faturas</title>
    <meta name="description" content="Extraia e descarregue automaticamente faturas de ficheiros PDF.">
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <!-- PDF.js CDN -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.min.js"></script>
    <script>
        pdfjsLib.GlobalWorkerOptions.workerSrc = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js';
    </script>
    
    <style>
        :root {
            --primary: #6366f1;
            --primary-hover: #4f46e5;
            --bg-color: #0f172a;
            --surface: rgba(30, 41, 59, 0.7);
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --success: #10b981;
            --border: rgba(255, 255, 255, 0.1);
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: 'Inter', sans-serif;
            background-color: var(--bg-color);
            background-image: 
                radial-gradient(at 0% 0%, rgba(99, 102, 241, 0.15) 0px, transparent 50%),
                radial-gradient(at 100% 100%, rgba(16, 185, 129, 0.1) 0px, transparent 50%);
            color: var(--text-main);
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 2rem;
            overflow-x: hidden;
        }

        .container {
            width: 100%;
            max-width: 600px;
            background: var(--surface);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid var(--border);
            border-radius: 24px;
            padding: 3rem 2rem;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
            text-align: center;
            transform: translateY(0);
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        }

        .container:hover {
            box-shadow: 0 30px 60px -15px rgba(0, 0, 0, 0.6);
            border-color: rgba(255, 255, 255, 0.15);
        }

        h1 {
            font-size: 2.25rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
            background: linear-gradient(to right, #818cf8, #c084fc);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            letter-spacing: -0.025em;
        }

        p.subtitle {
            color: var(--text-muted);
            margin-bottom: 2.5rem;
            font-size: 1.05rem;
            line-height: 1.5;
        }

        .drop-zone {
            border: 2px dashed var(--primary);
            border-radius: 16px;
            padding: 3.5rem 2rem;
            background: rgba(99, 102, 241, 0.05);
            cursor: pointer;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }

        .drop-zone.dragover {
            background: rgba(99, 102, 241, 0.15);
            border-color: #818cf8;
            transform: scale(1.02);
        }

        .drop-zone.processing {
            border-style: solid;
            border-color: var(--success);
            background: rgba(16, 185, 129, 0.05);
            cursor: default;
        }

        .icon-container {
            width: 70px;
            height: 70px;
            background: rgba(99, 102, 241, 0.1);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 1.5rem auto;
            color: var(--primary);
            transition: all 0.3s ease;
        }

        .drop-zone:hover .icon-container {
            transform: translateY(-5px);
            background: rgba(99, 102, 241, 0.2);
        }

        .drop-zone h3 {
            font-size: 1.25rem;
            font-weight: 600;
            margin-bottom: 0.5rem;
        }

        .drop-zone p {
            color: var(--text-muted);
            font-size: 0.95rem;
        }

        #file-input {
            display: none;
        }

        /* Results Area */
        #results {
            display: none;
            margin-top: 2rem;
            animation: fadeIn 0.5s ease;
        }

        .stats-card {
            background: rgba(0, 0, 0, 0.2);
            border-radius: 12px;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            border: 1px solid var(--border);
        }

        .stats-number {
            font-size: 3rem;
            font-weight: 700;
            color: var(--success);
            line-height: 1;
            margin-bottom: 0.5rem;
        }

        .stats-text {
            color: var(--text-muted);
            font-weight: 500;
        }

        .btn {
            background: var(--primary);
            color: white;
            border: none;
            padding: 1rem 2rem;
            font-size: 1.1rem;
            font-weight: 600;
            border-radius: 12px;
            cursor: pointer;
            width: 100%;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 0.75rem;
            transition: all 0.3s ease;
            box-shadow: 0 4px 6px -1px rgba(99, 102, 241, 0.3), 0 2px 4px -1px rgba(99, 102, 241, 0.2);
        }

        .btn:hover {
            background: var(--primary-hover);
            transform: translateY(-2px);
            box-shadow: 0 10px 15px -3px rgba(99, 102, 241, 0.4), 0 4px 6px -2px rgba(99, 102, 241, 0.2);
        }
        
        .btn:active {
            transform: translateY(0);
        }

        .btn-secondary {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid var(--border);
            margin-top: 1rem;
            box-shadow: none;
        }

        .btn-secondary:hover {
            background: rgba(255, 255, 255, 0.1);
            box-shadow: none;
        }

        /* Loading Spinner */
        .spinner {
            display: none;
            width: 40px;
            height: 40px;
            border: 4px solid rgba(99, 102, 241, 0.2);
            border-left-color: var(--primary);
            border-radius: 50%;
            animation: spin 1s linear infinite;
            margin: 0 auto 1.5rem auto;
        }

        @keyframes spin {
            to { transform: rotate(360deg); }
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* SVG Icons */
        svg {
            width: 32px;
            height: 32px;
            stroke-width: 2;
        }
        
        .btn svg {
            width: 24px;
            height: 24px;
        }

        .security-badge {
            margin-top: 2rem;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 0.5rem;
            color: var(--text-muted);
            font-size: 0.85rem;
            opacity: 0.7;
        }
    </style>
</head>
<body>

    <div class="container">
        <h1>Extrator de Faturas</h1>
        <p class="subtitle">Arraste o seu PDF para extrair todos os links automaticamente.</p>

        <div id="drop-zone" class="drop-zone">
            <div id="icon-normal" class="icon-container">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
                </svg>
            </div>
            
            <div id="spinner" class="spinner"></div>

            <h3 id="dz-title">Arraste e largue o PDF aqui</h3>
            <p id="dz-text">ou clique para selecionar um ficheiro do seu computador</p>
            <input type="file" id="file-input" accept="application/pdf">
        </div>

        <div id="results">
            <div class="stats-card">
                <div class="stats-number" id="link-count">0</div>
                <div class="stats-text">Faturas prontas para descarregar!</div>
            </div>
            
            <button id="download-btn" class="btn">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                </svg>
                Descarregar Tudo Agora
            </button>
            
            <button id="reset-btn" class="btn btn-secondary">Extrair outro ficheiro</button>
        </div>
    </div>

    <div class="security-badge">
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
        </svg>
        100% Seguro: O ficheiro não é enviado para a internet. Tudo acontece no seu computador.
    </div>

    <script>
        const dropZone = document.getElementById('drop-zone');
        const fileInput = document.getElementById('file-input');
        const iconNormal = document.getElementById('icon-normal');
        const spinner = document.getElementById('spinner');
        const dzTitle = document.getElementById('dz-title');
        const dzText = document.getElementById('dz-text');
        const results = document.getElementById('results');
        const linkCount = document.getElementById('link-count');
        const downloadBtn = document.getElementById('download-btn');
        const resetBtn = document.getElementById('reset-btn');

        let extractedLinks = [];

        // Triggers the file input when clicking the drop zone
        dropZone.addEventListener('click', () => {
            if (!dropZone.classList.contains('processing')) {
                fileInput.click();
            }
        });

        // Handle file selection via click
        fileInput.addEventListener('change', (e) => {
            if (e.target.files.length > 0) {
                processFile(e.target.files[0]);
            }
        });

        // Drag and Drop Events
        ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
            dropZone.addEventListener(eventName, preventDefaults, false);
        });

        function preventDefaults(e) {
            e.preventDefault();
            e.stopPropagation();
        }

        ['dragenter', 'dragover'].forEach(eventName => {
            dropZone.addEventListener(eventName, () => {
                if (!dropZone.classList.contains('processing')) {
                    dropZone.classList.add('dragover');
                }
            }, false);
        });

        ['dragleave', 'drop'].forEach(eventName => {
            dropZone.addEventListener(eventName, () => {
                dropZone.classList.remove('dragover');
            }, false);
        });

        dropZone.addEventListener('drop', (e) => {
            if (!dropZone.classList.contains('processing')) {
                let dt = e.dataTransfer;
                let files = dt.files;
                
                if (files.length > 0) {
                    if (files[0].type === 'application/pdf' || files[0].name.toLowerCase().endsWith('.pdf')) {
                        processFile(files[0]);
                    } else {
                        alert("Por favor, selecione um ficheiro PDF.");
                    }
                }
            }
        });

        async function processFile(file) {
            // UI Transition to Loading
            dropZone.classList.add('processing');
            iconNormal.style.display = 'none';
            spinner.style.display = 'block';
            dzTitle.textContent = "A extrair faturas...";
            dzText.textContent = "Isto demora apenas um segundo.";
            
            extractedLinks = [];

            try {
                const objectUrl = URL.createObjectURL(file);
                const loadingTask = pdfjsLib.getDocument(objectUrl);
                const pdf = await loadingTask.promise;
                
                const uniqueUrls = new Set();

                for (let i = 1; i <= pdf.numPages; i++) {
                    const page = await pdf.getPage(i);
                    const annotations = await page.getAnnotations();
                    
                    annotations.forEach(anno => {
                        if (anno.subtype === 'Link' && anno.url) {
                            uniqueUrls.add(anno.url);
                        }
                    });
                }

                extractedLinks = Array.from(uniqueUrls);
                
                // Show Results
                dropZone.style.display = 'none';
                results.style.display = 'block';
                linkCount.textContent = extractedLinks.length;
                
                if (extractedLinks.length === 0) {
                    linkCount.textContent = "0";
                    linkCount.style.color = "#f43f5e";
                    dzTitle.textContent = "Nenhum link encontrado no PDF.";
                    downloadBtn.style.display = 'none';
                }

            } catch (error) {
                console.error("Erro ao processar PDF:", error);
                alert("Ocorreu um erro ao ler o PDF. Verifique se o ficheiro não está corrompido.");
                resetUI();
            }
        }

        downloadBtn.addEventListener('click', () => {
            if (extractedLinks.length === 0) return;
            
            let i = 0;
            const interval = setInterval(() => {
                if (i >= extractedLinks.length) {
                    clearInterval(interval);
                    downloadBtn.innerHTML = `
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7" />
                        </svg>
                        Concluído!
                    `;
                    downloadBtn.style.background = 'var(--success)';
                    return;
                }
                
                const a = document.createElement('a');
                a.href = extractedLinks[i];
                a.download = ''; 
                a.target = '_blank';
                document.body.appendChild(a);
                a.click();
                document.body.removeChild(a);
                
                i++;
            }, 500);
        });

        resetBtn.addEventListener('click', resetUI);

        function resetUI() {
            dropZone.style.display = 'block';
            results.style.display = 'none';
            dropZone.classList.remove('processing');
            iconNormal.style.display = 'flex';
            spinner.style.display = 'none';
            dzTitle.textContent = "Arraste e largue o PDF aqui";
            dzText.textContent = "ou clique para selecionar um ficheiro do seu computador";
            fileInput.value = '';
            
            // Reset download button
            downloadBtn.innerHTML = `
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                </svg>
                Descarregar Tudo Agora
            `;
            downloadBtn.style.background = 'var(--primary)';
        }
    </script>
</body>
</html>
