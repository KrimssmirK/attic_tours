function getVoices() {
  return new Promise(
    function (resolve, reject) {
      let synth = window.speechSynthesis
      let id

      id = setInterval(() => {
        if (synth.getVoices().length !== 0) {
          resolve(synth.getVoices().filter(voice => voice.lang === "en-US"))
          clearInterval(id);
        }
      }, 10)
    }
  )
}

function callApplicant() {
  getVoices().then(SpeechSynthesisVoices => {
    for (var i = 0; i < SpeechSynthesisVoices.length; i++) {
      if (SpeechSynthesisVoices[i].name == "Samantha") {
        return SpeechSynthesisVoices[i]
      }
    }
  }).then(SpeechSynthesisVoice => callApplicantHelper(SpeechSynthesisVoice))

  function callApplicantHelper(SpeechSynthesisVoice) {
    const templateSpeach = "japan visa applicant number"
    const message = new SpeechSynthesisUtterance(templateSpeach + UiState.current_queue.number + "please proceed to window number " + UiState.current_window.number)
    message.volume = 1
    message.pitch = 1.5
    message.rate = 0.8
    message.lang = "en-US"
    message.voice = SpeechSynthesisVoice
    speechSynthesis.speak(message)
  }
}

const UiState = {
  current_queue: null,
  current_window: null,
  windows: null
}

function updateUiState(data) {
  UiState.current_queue = data.current_queue
  UiState.current_window = data.current_window
  UiState.windows = data.windows
}

function caller(endpoint) {
  // fetch the data per second
  setInterval(() => {
    fetch(endpoint)
    .then(response => response.json())
    .then(data => updateUiState(data))
    .catch((error) => {
      console.error(`Could not get queue number: ${error}`);
    })
  }, 1_000)
}



let window_setter_flag = true

function observer(queue_number_dom_id, window_number_dom_id, windows_id, audio_id) {
  setInterval(() => {
    // update UI
    // update queue number
    const queue_number_dom = document.getElementById(queue_number_dom_id)
    queue_number_dom.innerText = UiState.current_queue.number 
    // update window number
    const window_number_dom = document.getElementById(window_number_dom_id)
    const window_template = "WINDOW "
    window_number_dom.innerText = window_template + UiState.current_window.number

    if (window_setter_flag && windows_id) {
      setWindow(windows_id)
    }

    // call??
    if (UiState.current_queue.call) {
      ring(audio_id)
    }    
  }, 500)
}

function ring(audioID) {
  const targetAudio = document.getElementById(audioID)
  targetAudio.play()
  targetAudio.setAttribute("onended", "callApplicant()")
}


function setWindow(windows_id) {
  const selectDOM = document.getElementById(windows_id)

  for (var i = 0; i < UiState.windows.length; i++) {
    const option = document.createElement("option")
    option.setAttribute("value", String(UiState.windows[i].id))
    option.innerText = "Window " + String(UiState.windows[i].number)
    selectDOM.appendChild(option)
  }
  window_setter_flag = false
}















