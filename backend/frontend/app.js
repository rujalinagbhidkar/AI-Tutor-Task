const chatBox = document.getElementById("chat-box");
const statusText = document.getElementById("status");
const robotVideo = document.getElementById("robot-video");

function addMessage(text, sender) {
  const msg = document.createElement("div");
  msg.classList.add("message", sender);
  msg.innerText = text;
  chatBox.appendChild(msg);
  chatBox.scrollTop = chatBox.scrollHeight;
}

function startVoice() {
  const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();

  recognition.lang = "en-US";

  // Listening
  statusText.innerText = "🎤 Listening...";
  recognition.start();

  recognition.onresult = async function(event) {
    const text = event.results[0][0].transcript;

    addMessage(text, "user");

    // Thinking
    statusText.innerText = "🧠 Thinking...";
    addMessage("Thinking...", "bot");

    try {
      // LLM call
      const response = await fetch(`/chat?query=${encodeURIComponent(text)}`);
      const data = await response.json();

      // Remove "Thinking..."
      chatBox.lastChild.remove();

      addMessage(data.response, "bot");

      // Speaking
      statusText.innerText = "🔊 Tutor is speaking...";
      robotVideo.currentTime = 0;
      robotVideo.play();

      // TTS (same text)
      const audioRes = await fetch("/speak", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(data.response)
      });

      const blob = await audioRes.blob();
      const audio = new Audio(URL.createObjectURL(blob));
      audio.play();

      audio.onended = () => {
        robotVideo.pause();
        robotVideo.currentTime = 0;
        statusText.innerText = "🤖 Ready";
      };

    } catch (err) {
      robotVideo.pause();
      statusText.innerText = "❌ Error";
      addMessage("Error connecting to server", "bot");
    }
  };
}