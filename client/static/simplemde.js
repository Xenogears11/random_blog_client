//Initialize text editor

var simplemde = new SimpleMDE({
                element: document.getElementById("form_content"),
                placeholder: "Type your post here...",
                forceSync: true,
                spellChecker: false,
                toolbar: ["bold", "italic", "strikethrough", "|",
                    "heading", "horizontal-rule", "|",
                    "unordered-list", "ordered-list", "|",
                    "link", "image", "|",
                    "preview", "guide"
                ]
        });;