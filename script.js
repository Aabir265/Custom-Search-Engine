const form = document.getElementById("searchForm");
const input = document.getElementById("searchInput");
const resultsContainer = document.getElementById("results");

form.addEventListener("submit", async (event) => {
  event.preventDefault(); // it allows no page dosen't divert to an external page
const query = input.value.trim();
if (!query){
  input.focus(); // returns back the search bar if no query is there
  resultsContainer.textContent = "Please enter a search topic.";
        return;
}
resultsContainer.replaceChildren();
resultsContainer.textContent = "Searching...";


try {
        const response = await fetch("/search", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ query: query })
        });
        if (!response.ok) {
            throw new Error("Network response was not ok");
        }
        const data = await response.json();
        const results = data.results;



if(results.length === 0){
  resultsContainer.textContent = "No results found.";
  return;
}

resultsContainer.replaceChildren();
results.forEach((result) => {
  const resultElement = document.createElement("div");
const title = document.createElement("h3");
title.textContent = result.title;
const link = document.createElement("a");
link.href = result.url;
link.textContent = "Find out more";
link.target = "_blank";
link.rel = "noopener noreferrer";
resultElement.appendChild(title);
resultElement.appendChild(link);
resultsContainer.appendChild(resultElement);
});

} catch (error) {
  console.error("Search failed:", error);
  resultsContainer.textContent ="Something went wrong. Please try again.";
}

});
