
let counnter = 1;

function addNewAQ() {
    if (counnter <= 3) { // Limit to only three more inputs
        let container = document.createElement("div");
        container.classList.add("form-group", "added-input");

        let newNode = document.createElement("textarea");
        newNode.classList.add("form-control", "eqFeild", "mt-2");
        newNode.setAttribute("placeholder", " ");
        newNode.setAttribute("name", "aq_" + counnter); // Unique name attribute

        let newDateInput = document.createElement('input');
        newDateInput.setAttribute('type', 'date');
        newDateInput.setAttribute('class', 'form-control eqFeild');
        newDateInput.setAttribute('name', 'aq_date_' + counnter); // Unique name attribute for the date input

        let deleteButton = document.createElement("button");
        deleteButton.classList.add("btn", "btn-danger", "btn-sm");
        deleteButton.textContent = "حذف";
        deleteButton.onclick = function() {
            container.remove();
            counnter--; // Decrement the counter when removing an input
            if (counnter <= 3) {
                addAQbtn.disabled = false; // Enable the "إضافة +" button if the limit is not reached
            }
        };

        container.appendChild(newNode);
        container.appendChild(newDateInput);
        container.appendChild(deleteButton);

        let AQ = document.getElementById('AddAQ');
        let addAQbtn = document.getElementById('aqAddbtn');
        AQ.insertBefore(container, addAQbtn);

        counnter++; // Increment the counter for the next set of inputs
        if (counnter > 3) {
            addAQbtn.disabled = true; // Disable the "إضافة +" button when the limit is reached
        }
    }
}





function addNewWE() {
    // Create a new input for job title
    let jobTitleInput = document.createElement('input');
    jobTitleInput.setAttribute('type', 'text');
    jobTitleInput.setAttribute('placeholder', 'المسمى الوظيفي ');
    jobTitleInput.classList.add('form-control' , "mc2");

    // Create a new input for company name
    let companyNameInput = document.createElement('input');
    companyNameInput.setAttribute('type', 'text');
    companyNameInput.setAttribute('placeholder', 'إسم الشركة ');
    companyNameInput.classList.add('form-control', "mc2");

    // Create a new textarea for job description
    let jobDescriptionTextarea = document.createElement('textarea');
    jobDescriptionTextarea.setAttribute('placeholder', 'نبذه مختصرة عن وظيفتك في هذه الفتره');
    jobDescriptionTextarea.classList.add('form-control', 'weFeild1');

    // Create a new input for start date
    let startDateInput = document.createElement('input');
    startDateInput.setAttribute('type', 'date');
    startDateInput.classList.add('form-control', 'mv');

    // Create a new input for end date
    let endDateInput = document.createElement('input');
    endDateInput.setAttribute('type', 'date');
    endDateInput.classList.add('form-control', 'weFeild');

    // Create a new delete button
    let deleteButton = document.createElement('button');
    deleteButton.textContent = 'حذف';
    deleteButton.classList.add('btn', 'btn-danger');
    deleteButton.classList.add('del');
    deleteButton.onclick = function() {
        removeWE(this);
    };

    // Create a new input group
    let newInputGroup = document.createElement('div');
    newInputGroup.classList.add('input-group', 'mb-2');
    newInputGroup.appendChild(jobTitleInput);
    newInputGroup.appendChild(companyNameInput);
    newInputGroup.appendChild(jobDescriptionTextarea);

    // Append labels and inputs to the new input group
    let startDateLabel = document.createElement('label');
    startDateLabel.textContent = 'تاريخ البدء';
    newInputGroup.appendChild(startDateLabel);
    newInputGroup.appendChild(startDateInput);

    let endDateLabel = document.createElement('label');
    endDateLabel.textContent = 'تاريخ الانتهاء';
    newInputGroup.appendChild(endDateLabel);
    newInputGroup.appendChild(endDateInput);

    newInputGroup.appendChild(deleteButton);

    // Get the container and button
    let weInputs = document.getElementById('weInputs');
    weInputs.appendChild(newInputGroup);
}

function removeWE(button) {
    let inputGroup = button.parentElement;
    inputGroup.remove();
}














// Awards/Scholarship/Achievments
let counter = 1;

function Awardsfun() {
    if (counter <= 3) { // Check if the counter is less than or equal to three
        let newNode = document.createElement("div");
        newNode.classList.add("added-input");

        let newTextArea = document.createElement("textarea");
        newTextArea.classList.add("form-control", "eqFeild", "mt-2");
        newTextArea.setAttribute("placeholder", " ");
        newTextArea.setAttribute("name", "awards_" + counter); // Unique name attribute for textarea

        let newDateInput = document.createElement('input');
        newDateInput.setAttribute('type', 'date');
        newDateInput.setAttribute('class', 'form-control eqFeild');
        newDateInput.setAttribute('name', 'awards_date_' + counter); // Unique name attribute for date input

        let deleteButton = document.createElement("button");
        deleteButton.classList.add("btn", "btn-danger", "btn-sm", "delete-btn");
        deleteButton.textContent = "حذف ";
        deleteButton.onclick = function() {
            newNode.remove();
            counter--; // Decrement the counter when removing an input
            if (counter <= 3) {
                trofbtn.querySelector('button').disabled = false; // Enable the "إضافة +" button if the limit is not reached
            }
        };

        newNode.appendChild(newTextArea);
        newNode.appendChild(newDateInput);
        newNode.appendChild(deleteButton);

        let AQ = document.getElementById('Awardsfun');
        let trofbtn = document.getElementById('trofbtn');
        AQ.insertBefore(newNode, trofbtn);

        counter++; // Increment the counter for the next set of inputs
        if (counter > 3) {
            trofbtn.querySelector('button').disabled = true; // Disable the "إضافة +" button when the limit is reached
        }
    }
}


let countter = 1;
const maxInputs = 4;

function AddProject() {
    if (countter <= maxInputs) {
        let newNode = document.createElement("div");
        newNode.classList.add("form-group");

        let newTextArea = document.createElement("textarea");
        newTextArea.classList.add("form-control", "eqFeild");
        newTextArea.setAttribute('name', 'projname' + countter); // Set unique name
        newTextArea.setAttribute("placeholder", " ");

        let newDateInput = document.createElement('input');
        newDateInput.setAttribute('type', 'date');
        newDateInput.setAttribute('class', 'form-control eqFeild');
        newDateInput.setAttribute('name', 'projdate' + countter); // Set unique name

        let deleteButton = document.createElement("button");
        deleteButton.classList.add("btn", "btn-danger", "btn-sm");
        deleteButton.textContent = "حذف";
        deleteButton.onclick = function() {
            newNode.remove();
            countter--; // Decrement the counter when removing an input
            if (countter < maxInputs) {
                document.getElementById('projddbtn').querySelector('button').disabled = false; // Enable the "إضافة +" button if the limit is not reached
            }
        };

        newNode.appendChild(newTextArea);
        newNode.appendChild(newDateInput);
        newNode.appendChild(deleteButton);

        let AQ = document.getElementById('AddProject');
        AQ.insertBefore(newNode, document.getElementById('projddbtn'));

        counter++; // Increment the counter for the next set of inputs
        if (counter >= maxInputs) {
            document.getElementById('projddbtn').querySelector('button').disabled = true; // Disable the "إضافة +" button when the limit is reached
        }
    }
}