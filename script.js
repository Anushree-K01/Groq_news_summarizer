async function summarizeNews() {
    const newsText = document.getElementById("newsInput").value;
    const summaryOutput = document.getElementById("summaryOutput");
  
    if (!newsText.trim()) {
      summaryOutput.innerHTML = "Please enter some news text.";
      return;
    }
  
    try {
      console.log("Sending request to Flask...");
      
      const response = await fetch("http://127.0.0.1:5000/summarize-text", { 
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: newsText })
      });
  
      console.log("Response Status:", response.status); // Debugging
  
      const data = await response.json();
      console.log(" Response Data:", data); // Debugging
      
      //Fix UI update logic
      if (data && data.summary) {
        summaryOutput.innerHTML = `<strong>Summary:</strong> ${data.summary}`;
      } else {
        summaryOutput.innerHTML = " Error: No summary received.";
        console.error("No summary received from API");
      }
    } catch (error) {
      summaryOutput.innerHTML = " Error fetching summary!";
      console.error(" API Error:", error);
    }
  }
