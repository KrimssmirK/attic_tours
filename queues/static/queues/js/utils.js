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
    const templateSpeach = sessionStorage.getItem("call") == "japan" ? "Japan Visa applicant number " : "Korea Visa applicant number "
    const queue_number = sessionStorage.getItem("call") == "japan" ? UiState.current_japan_queue.number : UiState.current_korea_ticket_queue.number
    const window_number = sessionStorage.getItem("call") == "japan" ? UiState.current_japan_window.number : UiState.current_korea_ticket_window.number
    const message = new SpeechSynthesisUtterance(templateSpeach + queue_number + "please proceed to window number " + window_number)
    message.volume = 1
    message.pitch = 1.5
    message.rate = 0.8
    message.lang = "en-US"
    message.voice = SpeechSynthesisVoice
    speechSynthesis.speak(message)
  }
}

const UiState = {
  current_japan_queue: null,
  current_japan_window: null,
  current_korea_ticket_queue: null,
  current_korea_ticket_window: null,
  windows: null
}

function updateUiState(data) {
  UiState.current_japan_queue = data.current_japan_queue
  UiState.current_japan_window = data.current_japan_queue_window
  UiState.current_korea_ticket_queue = data.current_korea_ticket_queue
  UiState.current_korea_ticket_window = data.current_korea_ticket_queue_window
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

function observer(
  japan_queue_number_dom_id,
  japan_window_number_dom_id,
  korea_ticket_queue_number_dom_id,
  korea_ticket_window_number_dom_id,
  windows_id,
  audio_id
) {
  setInterval(() => {
    // update 2 UI components

    // (1)
    // update japan queue number
    const japan_queue_number_dom = document.getElementById(japan_queue_number_dom_id)
    japan_queue_number_dom.innerText = UiState.current_japan_queue.number
    // update japan window number
    const japan_window_number_dom = document.getElementById(japan_window_number_dom_id)
    const window_template = "WINDOW "
    japan_window_number_dom.innerText = window_template + UiState.current_japan_window.number

    // (2)
    // update korea ticket queue number
    const korea_ticket_queue_number_dom = document.getElementById(korea_ticket_queue_number_dom_id)
    korea_ticket_queue_number_dom.innerText = UiState.current_korea_ticket_queue.number
    // update japan window number
    const korea_ticket_window_number_dom = document.getElementById(korea_ticket_window_number_dom_id)
    korea_ticket_window_number_dom.innerText = window_template + UiState.current_korea_ticket_window.number

    // worker windows selection setter
    if (window_setter_flag && windows_id) {
      setWindow(windows_id.japan)
      setWindow(windows_id.korea)
      window_setter_flag = false
    }



    // call??
    if (UiState.current_japan_queue.call) {
      sessionStorage.setItem("call", "japan")
      ring(audio_id)
    }
    if (UiState.current_korea_ticket_queue.call) {
      sessionStorage.setItem("call", "korea")
      ring(audio_id)
    }
  }, 500)
}

function ring(audioID) {
  const targetAudio = document.getElementById(audioID)
  targetAudio.setAttribute("onended", "callApplicant()")
  targetAudio.play()
  // const promise = targetAudio.play();
  //   if(promise !== undefined){
  //       promise.then(() => {
  //           // Autoplay started
  //           targetAudio.play();
  //       }).catch(error => {
  //           // Autoplay was prevented.
  //           targetAudio.muted = true;
  //           targetAudio.play();
  //       });
  //   }
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















