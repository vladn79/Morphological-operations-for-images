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

    function submitInput() {
      var shapeValue = document.getElementById("shapeInput").value;
      document.getElementById("result1").innerText =  shapeValue;
      document.getElementById("inputPopup").style.display = "none";
    }