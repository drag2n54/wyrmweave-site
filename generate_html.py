def generate_html_from_videos(file_path="videos.txt", output_path="index.html"):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            videos = []
            for line in file:
                if "|" in line:
                    videos.append(line.strip().split("|"))
                else:
                    print(f"Skipping invalid line: {line.strip()}")

        html_content = """
        <!DOCTYPE html>
        <html lang="ar">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Wyrmweave Videos</title>
            <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap" rel="stylesheet">
            <style>
                body {
                    font-family: 'Cairo', Arial, sans-serif;
                    background-color: #2f2f2f;
                    color: #fff;
                    margin: 0;
                    padding: 0;
                }
                header {
                    text-align: center;
                    padding: 20px;
                    background: linear-gradient(135deg, #353330, #181818);
                    border-bottom: 3px solid #f39c12;
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    gap: 10px;
                }
                header img {
                    width: 100px;
                    height: auto;
                    cursor: pointer;
                    filter: drop-shadow(0 0 10px #f39c12);
                    transition: filter 0.3s ease-in-out;
                }
                header img:hover {
                    filter: drop-shadow(0 0 20px #ffcc00);
                }
                header h1 {
                    margin: 0;
                    color: #f1c40f;
                }
                #search-bar {
                    margin: 20px auto;
                    display: block;
                    padding: 10px;
                    width: 80%;
                    max-width: 600px;
                    border: 2px solid #f39c12;
                    border-radius: 10px;
                    background-color: #3f3f3f;
                    color: #f1c40f;
                    font-size: 16px;
                }
                #search-bar:focus {
                    outline: none;
                    box-shadow: 0 0 10px #ffcc00;
                }
                #video-gallery {
                    display: grid;
                    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                    gap: 20px;
                    padding: 20px;
                }
                .video-box {
                    background: #3f3f3f;
                    border-radius: 10px;
                    overflow: hidden;
                    text-align: center;
                    box-shadow: 0 8px 15px rgba(0, 0, 0, 0.4);
                    transition: transform 0.3s, box-shadow 0.3s;
                    border: 2px solid #f39c12;
                }
                .video-box:hover {
                    transform: scale(1.05);
                    box-shadow: 0 12px 20px rgba(255, 204, 0, 0.7),
                                0 0 30px rgba(255, 153, 51, 0.8),
                                0 0 60px rgba(255, 102, 0, 0.9);
                }
                iframe {
                    width: 100%;
                    height: 200px;
                    border: none;
                    border-bottom: 5px solid #f39c12;
                }
                p {
                    margin: 10px;
                    color: #f1c40f;
                }
                footer {
                    text-align: center;
                    padding: 10px;
                    background: #3f3f3f;
                    color: #f1c40f;
                    border-top: 3px solid #f39c12;
                }
            </style>
            <script>
                let typingTimeout; // Variable to store the timeout ID for typing sound

                function filterVideos() {
                    const searchInput = document.getElementById("search-bar").value.toLowerCase();
                    const videos = document.getElementsByClassName("video-box");
                    const audioTyping = document.getElementById("sfx-typing");

                    // Play typing sound
                    audioTyping.play();
                    clearTimeout(typingTimeout); // Clear previous timeout
                    typingTimeout = setTimeout(() => {
                        audioTyping.pause();
                        audioTyping.currentTime = 0;
                    }, 500); // Stop sound if no typing for 500ms

                    for (const video of videos) {
                        const title = video.querySelector("p").textContent.toLowerCase();
                        video.style.display = title.includes(searchInput) ? "block" : "none";
                    }
                }

                window.onload = () => {
                    const logo = document.querySelector("header img");
                    const videoBoxes = document.querySelectorAll(".video-box");
                    const audioLogoClick = document.getElementById("sfx-logo-click");
                    const audioHover = document.getElementById("sfx-hover");

                    logo.addEventListener("click", () => {
                        audioLogoClick.play();
                    });

                    videoBoxes.forEach(box => {
                        box.addEventListener("mouseover", () => {
                            audioHover.currentTime = 0; // Reset sound
                            audioHover.play();
                        });
                        box.addEventListener("mouseout", () => {
                            audioHover.pause();
                            audioHover.currentTime = 0; // Reset to start
                        });
                    });
                };
            </script>
        </head>
        <body>
            <!-- Audio Elements -->
            <audio id="sfx-logo-click" src="sfx/sfx2.mp3"></audio>
            <audio id="sfx-hover" src="sfx/sfx1.mp3" loop></audio>
            <audio id="sfx-typing" src="sfx/sfx3.mp3"></audio>

            <header>
                <a href="https://www.youtube.com/@Wyrmweave" target="_blank">
                    <img src="images/wyrmweave.png" alt="Wyrmweave Logo">
                </a>
                <h1>مرحبًا</h1>
            </header>
            <main>
                <input
                    type="text"
                    id="search-bar"
                    placeholder="ابحث عن فيديو..."
                    onkeyup="filterVideos()">
                <div id="video-gallery">
        """

        for video_id, title in videos:
            html_content += f"""
                    <div class="video-box">
                        <iframe src="https://www.youtube.com/embed/{video_id}" allowfullscreen></iframe>
                        <p>{title}</p>
                    </div>
            """

        html_content += """
                </div>
            </main>
            <footer>
                <p>© 2025 Wyrmweave. All rights reserved.</p>
            </footer>
        </body>
        </html>
        """

        with open(output_path, "w", encoding="utf-8") as output_file:
            output_file.write(html_content)
        print(f"HTML generated successfully: {output_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Generate the HTML file
generate_html_from_videos()
