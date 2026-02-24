const API_URL = 'http://localhost:8000/api/get-email-data';

let emailData = {
    subject: '',
    body: '',
    sender: '',
    category: '',
    priority: ''
};



Office.onReady((info) => {
    if (info.host === Office.HostType.Outlook) {
        loadEmailData();
        setupButton();
    }
});

function loadEmailData() {
    const item = Office.context.mailbox.item;

    if (typeof item.subject === 'string') {
        emailData.subject = item.subject;
        document.getElementById('item-subject').innerText = item.subject;
    } else {
        item.subject.getAsync(result => {
            if (result.status === Office.AsyncResultStatus.Succeeded) {
                emailData.subject = result.value;
                document.getElementById('item-subject').innerText = result.value;
            }
        });
    }

    const from = item.from;
    if (from && typeof from.emailAddress === 'string') {
        emailData.sender = from.emailAddress;
        document.getElementById('item-from').innerText = from.emailAddress;
    }

    item.body.getAsync('text', function(result) {
        if (result.status === Office.AsyncResultStatus.Succeeded) {
            emailData.body = result.value;
            document.getElementById('body-subject').innerText = result.value;
        }
    });

    if (item.attachments.length > 0) {
        let att = [];
        for (let i = 0; i < item.attachments.length; i++) {
            att.push(item.attachments[i].name);
        }
        document.getElementById('attachment-view').innerText = att.join(' , ');
    } else {
        document.getElementById('attachment-view').innerText = "This email does not contain any attachment";
    }

    const category = document.getElementById('category-selection');
    emailData.category = category.value;
    category.addEventListener('change', () => { emailData.category = category.value; });

    const priority = document.getElementById('priority-section');
    emailData.priority = priority.value;
    priority.addEventListener('change', () => { emailData.priority = priority.value; });
}

function setupButton() {
    document.getElementById('analyze-button')?.addEventListener('click', analyzeEmail);
}

async function analyzeEmail() {
    const resultsDiv = document.getElementById('results');

    if (!emailData.subject || !emailData.body) {
        resultsDiv.innerHTML = '<p style="color: red;">Please open an email first.</p>';
        return;
    }

    try {
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(emailData)
        });

        if (!response.ok) throw new Error(`HTTP ${response.status}`);

        const result = await response.json();
        resultsDiv.innerHTML = `
            <p><strong>📝 Summary:</strong> ${result.summary}</p>
            <p><strong>✅ Action Items:</strong></p>
            <ul>${result.action_items.map(item => `<li>${item}</li>`).join('')}</ul>
            <p><strong>💬 Suggested Reply:</strong> ${result.suggested_reply}</p>
        `;
    } catch (error) {
        resultsDiv.innerHTML = `<p style="color: red;">Error: ${error.message}</p>`;
    }
}
