document.addEventListener('DOMContentLoaded', function () {
  var linkTabButton = document.getElementById('enter-link-tab');
  var contentTabButton = document.getElementById('enter-content-tab');
  var linkContainer = document.getElementById('link-container');
  var contentContainer = document.getElementById('content-container');
  var messageContainer = document.getElementById('message-container');
  
  var linkInput = document.getElementById('link-input');
  var contentInput = document.getElementById('content-input');
  var sourceInput = document.getElementById('source-input');
  var isVerifiedCheckbox = document.getElementById('is-verified-checkbox');

  var submitLinkButton = document.getElementById('submit-link-button');
  var submitContentButton = document.getElementById('submit-content-button');

  linkTabButton.addEventListener('click', function () {
    linkContainer.style.display = 'block';
    contentContainer.style.display = 'none';
    hideMessage();
  });

  contentTabButton.addEventListener('click', function () {
    linkContainer.style.display = 'none';
    contentContainer.style.display = 'block';
    hideMessage();
  });

  submitLinkButton.addEventListener('click', function () {
    var news_url = linkInput.value.trim();
    var is_verified = isVerifiedCheckbox.checked;

    if (news_url) {
      sendDataToServer({ news_url, is_verified });
    } else {
      showMessage('Please enter a link before submitting.', 'danger');
    }
  });

  submitContentButton.addEventListener('click', function () {
    var content = contentInput.value.trim();
    var source = sourceInput.value.trim();
    var isVerified = isVerifiedCheckbox.checked;

    if (content && source) {
      sendDataToServer({ content, source, isVerified });
    } else {
      showMessage('Please enter content and source before submitting.', 'danger');
    }
  });

  async function sendDataToServer(data) {
    showLoading(); // Show loading overlay before sending data
  
    const apiUrl = 'http://localhost:4003/news/collect';
    const params = new URLSearchParams(data);
    const urlWithParams = `${apiUrl}?${params.toString()}`;
  
    const options = {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      mode: 'cors',
    };
  
    try {
      const response = await fetch(urlWithParams, options);
      const result = await response.json();
      console.log('Data sent to server:', result);
      showMessage('Data submitted successfully!', 'success');
    } catch (error) {
      console.error('Error sending data to server:', error);
      showMessage('Error submitting data. Please try again.', 'error');
    } finally {
      hideLoading(); // Hide loading overlay after response (success or error)
    }
  }
  
  

  function showMessage(message, type) {
    messageContainer.textContent = message;
    messageContainer.style.backgroundColor = type === 'success' ? '#28a745' : '#dc3545'; // Green or Red
    messageContainer.style.display = 'block';

    setTimeout(hideMessage, 3000); // Hide after 3 seconds
  }

  function hideMessage() {
    messageContainer.style.display = 'none';
  }

  function showLoading() {
    var loadingOverlay = document.getElementById('loading-overlay');
    loadingOverlay.style.display = 'flex';
  }

  function hideLoading() {
    var loadingOverlay = document.getElementById('loading-overlay');
    loadingOverlay.style.display = 'none';
  }

  // Show link input by default
  linkTabButton.click();
});
