(function(document) {
  var toggle = document.querySelector('.sidebar-toggle');
  var sidebar = document.querySelector('#sidebar');
  var checkbox = document.querySelector('#sidebar-checkbox');

  if (checkbox && window.innerWidth > 1480)
    checkbox.checked = true;

  document.addEventListener('click', function(e) {
    var target = e.target;

    if(!checkbox || !checkbox.checked ||
       (sidebar && sidebar.contains(target)) ||
       (target === checkbox || target === toggle)) return;

    checkbox.checked = false;
  }, false);

  /* Collapse/expand chapter lesson lists in the menubar */
  if (sidebar) {
    sidebar.addEventListener('click', function(e) {
      var caret = e.target.closest('.sidebar-nav-caret');
      if (!caret || !sidebar.contains(caret)) return;
      e.preventDefault();
      e.stopPropagation();
      var group = caret.closest('.sidebar-nav-group');
      if (!group) return;
      var open = group.classList.toggle('is-open');
      caret.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }
})(document);
