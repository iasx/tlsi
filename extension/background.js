// *---------------------------------------------------------------------------* Functions

function process() {
  text = window.getSelection().toString();

  fetch("http://127.0.0.1:8000", {
    method: "POST",
    body: JSON.stringify({ text: text }),
    headers: {
      "Content-Type": "application/json;charset=utf-8",
    },
  }).then((ok) =>
    ok.text().then((data) => {
      alert(data);
    })
  );
}

// *---------------------------------------------------------------------------* Action Handler

chrome.action.onClicked.addListener((tab) => {
  chrome.scripting.executeScript({
    target: { tabId: tab.id },
    function: process,
  });
});

// *---------------------------------------------------------------------------* Shortcut Handler

chrome.commands.onCommand.addListener((cmd, tab) => {
  if (cmd === "summarize") {
    chrome.scripting.executeScript({
      target: { tabId: tab.id },
      function: process,
    });
  }
});

// *---------------------------------------------------------------------------* Context Menu Handler

chrome.runtime.onInstalled.addListener(() => {
  chrome.contextMenus.create({
    id: "tldr",
    title: "Summarize",
    contexts: ["selection"],
  });
});

chrome.contextMenus.onClicked.addListener((item, tab) => {
  if (item.menuItemId === "tldr") {
    chrome.scripting.executeScript({
      target: { tabId: tab.id },
      function: process,
    });
  }
});
