const headers = document.querySelectorAll(".accordion-header");

headers.forEach((header) => {
  header.addEventListener("click", () => {
    const body = header.nextElementSibling;

    // Optionally close all first - it just romoves any show on the class name selector
    document.querySelectorAll(".accordion-body").forEach((b) => {
      if (b !== body) b.classList.remove("show");
    });

    // Toggle this one
    body.classList.toggle("show");
  });
});
