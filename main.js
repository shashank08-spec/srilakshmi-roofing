/*!
 * Sri Lakshmi Roofing Industry — front-end interactions
 * Vanilla JS, no framework dependency — keeps the site fast-loading.
 */
(function () {
  "use strict";

  document.addEventListener("DOMContentLoaded", function () {
    initLoader();
    initNav();
    initScrollEffects();
    initBackToTop();
    initReveal();
    initAccordion();
    initProductFilter();
    initGalleryFilterAndLightbox();
    initFormValidation();
  });

  /* ---------------- Page loader ---------------- */
  function initLoader() {
    var loader = document.getElementById("page-loader");
    if (!loader) return;
    window.addEventListener("load", function () {
      setTimeout(function () { loader.classList.add("is-hidden"); }, 250);
    });
    // Fallback in case 'load' already fired
    if (document.readyState === "complete") {
      loader.classList.add("is-hidden");
    }
  }

  /* ---------------- Nav (mobile menu + sticky shadow) ---------------- */
  function initNav() {
    var navbar = document.querySelector(".navbar");
    var toggle = document.querySelector(".nav-toggle");
    var links = document.querySelector(".nav-links");
    var overlay = document.querySelector(".nav-overlay");

    if (toggle && links && overlay) {
      toggle.addEventListener("click", function () {
        var isOpen = links.classList.toggle("is-open");
        overlay.classList.toggle("is-open", isOpen);
        toggle.setAttribute("aria-expanded", isOpen ? "true" : "false");
        document.body.style.overflow = isOpen ? "hidden" : "";
      });
      overlay.addEventListener("click", function () {
        links.classList.remove("is-open");
        overlay.classList.remove("is-open");
        toggle.setAttribute("aria-expanded", "false");
        document.body.style.overflow = "";
      });
      links.querySelectorAll("a").forEach(function (a) {
        a.addEventListener("click", function () {
          links.classList.remove("is-open");
          overlay.classList.remove("is-open");
          document.body.style.overflow = "";
        });
      });
    }

    if (navbar) {
      var onScroll = function () {
        navbar.classList.toggle("is-scrolled", window.scrollY > 12);
      };
      onScroll();
      window.addEventListener("scroll", onScroll, { passive: true });
    }
  }

  function initScrollEffects() {
    // placeholder hook for future parallax / scroll-linked effects
  }

  /* ---------------- Back to top ---------------- */
  function initBackToTop() {
    var btn = document.querySelector(".fab--top");
    if (!btn) return;
    window.addEventListener("scroll", function () {
      btn.classList.toggle("is-visible", window.scrollY > 480);
    }, { passive: true });
    btn.addEventListener("click", function () {
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  }

  /* ---------------- Scroll reveal animations ---------------- */
  function initReveal() {
    var items = document.querySelectorAll(".reveal");
    if (!items.length) return;

    if (!("IntersectionObserver" in window)) {
      items.forEach(function (el) { el.classList.add("is-revealed"); });
      return;
    }

    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-revealed");
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -40px 0px" });

    items.forEach(function (el) { observer.observe(el); });
  }

  /* ---------------- FAQ accordion ---------------- */
  function initAccordion() {
    var items = document.querySelectorAll(".accordion-item");
    items.forEach(function (item) {
      var trigger = item.querySelector(".accordion-trigger");
      var panel = item.querySelector(".accordion-panel");
      if (!trigger || !panel) return;

      trigger.addEventListener("click", function () {
        var isOpen = item.classList.contains("is-open");

        items.forEach(function (other) {
          other.classList.remove("is-open");
          var otherPanel = other.querySelector(".accordion-panel");
          if (otherPanel) otherPanel.style.maxHeight = null;
          var otherTrigger = other.querySelector(".accordion-trigger");
          if (otherTrigger) otherTrigger.setAttribute("aria-expanded", "false");
        });

        if (!isOpen) {
          item.classList.add("is-open");
          panel.style.maxHeight = panel.scrollHeight + "px";
          trigger.setAttribute("aria-expanded", "true");
        }
      });
    });
  }

  /* ---------------- Product filter + search ---------------- */
  function initProductFilter() {
    var grid = document.querySelector("[data-product-grid]");
    if (!grid) return;

    var chips = document.querySelectorAll(".filter-chip[data-filter]");
    var searchInput = document.querySelector("[data-product-search]");
    var cards = grid.querySelectorAll("[data-category]");
    var noResults = document.querySelector(".no-results");
    var activeFilter = "all";

    function applyFilters() {
      var term = (searchInput && searchInput.value || "").trim().toLowerCase();
      var visibleCount = 0;

      cards.forEach(function (card) {
        var category = card.getAttribute("data-category");
        var haystack = (card.getAttribute("data-search") || "").toLowerCase();
        var matchesCategory = activeFilter === "all" || category === activeFilter;
        var matchesSearch = !term || haystack.indexOf(term) !== -1;
        var visible = matchesCategory && matchesSearch;
        card.style.display = visible ? "" : "none";
        if (visible) visibleCount++;
      });

      if (noResults) noResults.classList.toggle("is-visible", visibleCount === 0);
    }

    chips.forEach(function (chip) {
      chip.addEventListener("click", function () {
        chips.forEach(function (c) { c.classList.remove("is-active"); });
        chip.classList.add("is-active");
        activeFilter = chip.getAttribute("data-filter");
        applyFilters();
      });
    });

    if (searchInput) {
      searchInput.addEventListener("input", applyFilters);
    }
  }

  /* ---------------- Gallery filter + lightbox ---------------- */
  function initGalleryFilterAndLightbox() {
    var galleryChips = document.querySelectorAll(".gallery-filters .filter-chip");
    var items = document.querySelectorAll(".gallery-item");

    galleryChips.forEach(function (chip) {
      chip.addEventListener("click", function () {
        galleryChips.forEach(function (c) { c.classList.remove("is-active"); });
        chip.classList.add("is-active");
        var filter = chip.getAttribute("data-filter");
        items.forEach(function (item) {
          var cat = item.getAttribute("data-category");
          item.style.display = (filter === "all" || cat === filter) ? "" : "none";
        });
      });
    });

    var lightbox = document.querySelector(".lightbox");
    if (!lightbox) return;
    var lightboxBody = lightbox.querySelector("[data-lightbox-body]");
    var closeBtn = lightbox.querySelector(".lightbox__close");

    items.forEach(function (item) {
      item.addEventListener("click", function () {
        var caption = item.getAttribute("data-caption") || "";
        if (lightboxBody) lightboxBody.textContent = caption;
        lightbox.classList.add("is-open");
        document.body.style.overflow = "hidden";
      });
    });

    function closeLightbox() {
      lightbox.classList.remove("is-open");
      document.body.style.overflow = "";
    }

    if (closeBtn) closeBtn.addEventListener("click", closeLightbox);
    lightbox.addEventListener("click", function (e) {
      if (e.target === lightbox) closeLightbox();
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") closeLightbox();
    });
  }

  /* ---------------- Client-side form validation ---------------- */
  function initFormValidation() {
    var forms = document.querySelectorAll("[data-validate]");

    forms.forEach(function (form) {
      form.addEventListener("submit", function (e) {
        var valid = true;
        var requiredFields = form.querySelectorAll("[required]");

        requiredFields.forEach(function (field) {
          var wrapper = field.closest(".field");
          var value = (field.value || "").trim();
          var isValid = value.length > 0;

          if (field.type === "email" && value) {
            isValid = /^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(value);
          }
          if (field.type === "tel" && value) {
            isValid = /^[+]?[0-9\s-]{7,15}$/.test(value);
          }

          if (wrapper) wrapper.classList.toggle("has-error", !isValid);
          if (!isValid) valid = false;
        });

        if (!valid) {
          e.preventDefault();
          var firstError = form.querySelector(".has-error");
          if (firstError) {
            firstError.scrollIntoView({ behavior: "smooth", block: "center" });
          }
        }
      });

      form.querySelectorAll("[required]").forEach(function (field) {
        field.addEventListener("input", function () {
          var wrapper = field.closest(".field");
          if (wrapper) wrapper.classList.remove("has-error");
        });
      });
    });
  }
})();
