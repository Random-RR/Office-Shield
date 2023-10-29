document.addEventListener('DOMContentLoaded', function () {
  // Get the open button element
  var openButton = document.getElementById('openButton');

  // Add a click event listener to the open button
  openButton.addEventListener('click', function () {
    // Open a new window with the desired URL
    var newWindow = window.open('http://127.0.0.1:5000', 'OfficeShield', 'width=400,height=650');
    
    // Ensure that the new window is not null
    if (newWindow) {
      // Focus the new window
      newWindow.focus();
    }
  });
});

