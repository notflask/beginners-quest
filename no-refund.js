async function sendRefund() {
  try {
    let res = await fetch("https://no-refund-web.2024-bq.ctfcompetition.com/refund", {
      method: "POST",
      headers: {
        "content-type": "application/x-www-form-urlencoded"
      },
      body: "reason=delay&ticket_id=85cc3c46f7657a8a962d3b2b299d9be8"
    });

    let text = await res.text();
    console.log(text);
  } catch (err) {
    console.error("error:", err);
  }
}

sendRefund();

