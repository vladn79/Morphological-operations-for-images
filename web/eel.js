function toggleDropdown() {
      document.getElementById("dropdownContent").classList.toggle("show");
    }

function showInput(shape) {
      document.getElementById("inputPopup").style.display = "block";
      document.getElementById("shapeInput").focus();
      document.getElementById("shapeInput").value = shape;
    }
    
    var previousValue = ""; 


    function displayResult(operation) {
      var currentValue = document.getElementById("result").innerText;
      previousValue = currentValue; 
      document.getElementById("result").innerText = operation;
    }

    function showInput(shape) {
      document.getElementById("inputPopup").style.display = "block";
      document.getElementById("shapeInput").focus();
      document.getElementById("shapeInput").value = shape;
    }

      eel.expose(submitInput);
   eel.expose(getResultsArray); // Експорт функції для отримання масиву результатів

    function submitInput() {
        var shapeValue = document.getElementById("shapeInput").value;
        var resultValue = document.getElementById("result").innerText;
        var result1Value = document.getElementById("result1").innerText;
     eel.add_result_to_array(shapeValue, resultValue, result1Value); // Виклик Python-функції
        document.getElementById("result1").innerText = shapeValue;
        document.getElementById("inputPopup").style.display = "none";
    }

    getResultsArray().then(displayResultsArray);

    function displayResultsArray(results) {
        console.log(results); 
    }
    document.addEventListener('DOMContentLoaded', function () {
      var fileInput = document.getElementById('fileInput');
      var uploadButton = document.getElementById('uploadButton');
      var uploadStatus = document.getElementById('uploadStatus');
      var imagePreview = document.getElementById('imagePreview');
  
      uploadButton.addEventListener('click', function () {
          uploadFile();
      });
  
      fileInput.addEventListener('change', function () {
          previewImage();
      });
  
      function uploadFile() {
          var file = fileInput.files[0];
          var formData = new FormData();
          formData.append('file', file);
  
          var xhr = new XMLHttpRequest();
          xhr.open('POST', '/upload', true); 
          xhr.onload = function () {
              if (xhr.status === 200) {
                  uploadStatus.textContent = 'File uploaded successfully!';
              } else {
                  uploadStatus.textContent = 'Upload failed!';
              }
          };
          xhr.send(formData);
      }
  
      function previewImage() {
          var file = fileInput.files[0];
          var reader = new FileReader();
  
          reader.onload = function (event) {
              var imageUrl = event.target.result;
              var img = document.createElement('img');
              img.src = imageUrl;
              img.style.maxWidth = '300px'; 
              imagePreview.innerHTML = ''; 
              imagePreview.appendChild(img);
          };
  
          reader.readAsDataURL(file);
      }
  });
  