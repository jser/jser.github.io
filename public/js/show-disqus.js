(function (document) {
    "use strict";
    var commentsButton = document.getElementById("js-comment-button");
    // Click event handler
    commentsButton.addEventListener('click', function () {
        // Create comments container
        var disqusContainer = document.createElement('div'),
            disqus_shortname = 'jser',
            dsq = document.createElement('script');
        disqusContainer.setAttribute('id', 'disqus_thread');
        // Disqus
        dsq.type = 'text/javascript';
        dsq.async = true;
        dsq.src = '//' + disqus_shortname + '.disqus.com/embed.js';
        (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);
        // Append container to body
        document.getElementById("js-disqus-embed").appendChild(disqusContainer);
        // Remove button
        this.parentNode.removeChild(this);
    }, false);
})(document);
