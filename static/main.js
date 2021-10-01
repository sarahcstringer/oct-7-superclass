window.addEventListener("load", () => {
  // initialize number of participants with local video.
  // we can have a max of six participants.
  let availableYarn = [1, 2, 3, 4, 5, 6];
  const roomName = "Superclass!";
  const identity = document.getElementById("identity");
  const identityDiv = document.getElementById("identity-div");
  const joinButton = document.getElementById("join");

  joinButton.addEventListener("click", connect);

  async function connect () {
    identityDiv.style.display = "none";
    joinButton.style.display = "none";
  }

  // tidy up helper functions for when a participant disconnects
  // or closes the page
  function participantDisconnected(participant) {
    participant.removeAllListeners();
    const el = document.getElementById(`yarn-${participant.number}`);
    el.innerHTML = "";
    availableYarn.push(participant.number);
  }

  // helper to find a spot on the page to display participant video
  function findNextAvailableYarn(participant) {
    const index = Math.floor(Math.random() * availableYarn.length);
    const choice = availableYarn[index];
    availableYarn = availableYarn.filter((e) => e != choice);
    participant.number = choice;
  }
});
