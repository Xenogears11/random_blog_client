//Show alert

document.addEventListener("DOMContentLoaded", function() {

                        var alert = document.createElement("div");
                        alert.setAttribute('class', 'alert alert-success alert-dismissible ' +
                            'blog-alert fade show');
                        alert.setAttribute('role', 'alert');
                        var msg = document.getElementById("alerts").getAttribute('data-msg')
                        alert.innerText = msg;

                        var btn = document.createElement('button');
                        btn.setAttribute('type', 'button');
                        btn.setAttribute('class', 'close');
                        btn.setAttribute('data-dismiss', 'alert');
                        btn.setAttribute('aria-label', 'Close');

                        var span = document.createElement('span');
                        btn.setAttribute('aria-hidden', 'true');
                        btn.innerText = '×';

                        btn.appendChild(span);
                        alert.appendChild(btn);
                        document.body.appendChild(alert);

                        setTimeout(function() {
                            document.body.removeChild(alert)
                        }, 3000);

                    });