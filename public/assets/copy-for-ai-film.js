/* The film on /copy-for-ai/ (scripts/brand_film_copy_for_ai.py, website #366).
   A phone-width window gets the 720p file (the <video> names it in data-small); a wider one keeps the
   1080p file in its <source>. The film then plays muted and looped, unless the visitor asked for less
   motion (prefers-reduced-motion: reduce): the page has no `autoplay` attribute, so that visitor, and one
   whose browser does not run this script, sees the poster, and the controls play the film.
   External on purpose: the CSP's script-src is 'self'. */
(function () {
  'use strict';
  var video = document.querySelector('video[data-small]');
  if (!video || !window.matchMedia) return;
  if (window.matchMedia('(max-width: 899.98px)').matches) {
    // A `src` on the <video> overrides its <source>; nothing has been fetched yet (preload="none").
    video.src = video.getAttribute('data-small');
  }
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  video.muted = true;
  var started = video.play();
  // A browser may still refuse (Low Power Mode on iPhone, a data saver): the poster and controls stay.
  if (started && typeof started.catch === 'function') started.catch(function () {});
}());
