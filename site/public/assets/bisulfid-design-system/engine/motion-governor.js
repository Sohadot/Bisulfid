/**
 * Bisulfid Motion Governor — vanilla JS, no dependencies.
 * Controls visual motion states only. Does not mutate source/claim truth.
 * Respects prefers-reduced-motion. Fail-safe when JS disabled.
 */
(function (global) {
  "use strict";

  var REDUCED_QUERY = "(prefers-reduced-motion: reduce)";

  function prefersReducedMotion() {
    if (typeof global.matchMedia !== "function") {
      return true;
    }
    return global.matchMedia(REDUCED_QUERY).matches;
  }

  /**
   * Apply motion class to element if motion allowed.
   * Never adds approval or source-state classes.
   */
  function applyMotionState(element, motionClass) {
    if (!element || !motionClass) {
      return;
    }
    if (prefersReducedMotion()) {
      element.classList.remove(motionClass);
      element.setAttribute("data-bs-motion", "reduced");
      return;
    }
    element.classList.add(motionClass);
    element.setAttribute("data-bs-motion", "active");
  }

  /**
   * Missing-E boundary motion — spelling boundary emphasis only.
   */
  function initMissingEBoundary(selector) {
    if (prefersReducedMotion()) {
      return;
    }
    var nodes = document.querySelectorAll(selector || ".bs-motion-missing-e");
    for (var i = 0; i < nodes.length; i++) {
      applyMotionState(nodes[i], "bs-motion-missing-e--active");
    }
  }

  /**
   * Relation pulse — only on elements with data-link-status (data-bound).
   */
  function initRelationPulse(selector) {
    if (prefersReducedMotion()) {
      return;
    }
    var edges = document.querySelectorAll(
      selector || ".bs-relation-lattice__edge[data-link-status]"
    );
    for (var j = 0; j < edges.length; j++) {
      edges[j].setAttribute("data-bs-motion", "pulse-eligible");
    }
  }

  function init() {
    initMissingEBoundary();
    initRelationPulse();
  }

  if (typeof global.matchMedia === "function") {
    global.matchMedia(REDUCED_QUERY).addEventListener("change", function () {
      init();
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }

  global.BisulfidMotionGovernor = {
    prefersReducedMotion: prefersReducedMotion,
    applyMotionState: applyMotionState,
    init: init,
  };
})(typeof window !== "undefined" ? window : globalThis);
