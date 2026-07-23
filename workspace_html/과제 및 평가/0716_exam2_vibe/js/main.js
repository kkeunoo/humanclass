document.addEventListener("DOMContentLoaded", () => {
    document.body.classList.add("loaded");

    const loader = document.querySelector(
        ".loader, .loading, .preloader, #loader"
    );

    if (loader) {
        loader.style.display = "none";
    }

    document.querySelectorAll(".reveal").forEach((element) => {
        element.classList.add("show");
    });
});

document.addEventListener("DOMContentLoaded", () => {
    /* =========================
       기본 화면 표시
    ========================= */

    document.body.classList.add("loaded");

    const revealElements = document.querySelectorAll(".reveal");

    if ("IntersectionObserver" in window) {
        const revealObserver = new IntersectionObserver(
            (entries, observer) => {
                entries.forEach((entry) => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add("show");
                        observer.unobserve(entry.target);
                    }
                });
            },
            {
                threshold: 0.1,
                rootMargin: "0px 0px -40px 0px"
            }
        );

        revealElements.forEach((element) => {
            revealObserver.observe(element);
        });
    } else {
        revealElements.forEach((element) => {
            element.classList.add("show");
        });
    }

    /* 첫 화면 요소가 숨겨지는 문제 방지 */
    setTimeout(() => {
        document.querySelectorAll(".reveal").forEach((element) => {
            const rect = element.getBoundingClientRect();

            if (rect.top < window.innerHeight) {
                element.classList.add("show");
            }
        });
    }, 100);

    /* =========================
       Hero Typing
    ========================= */

    const typingTarget = document.querySelector(
        ".typing, .typing-text, [data-typing]"
    );

    if (typingTarget) {
        const words = [
            "HTML",
            "CSS",
            "JavaScript",
            "React",
            "Spring Boot",
            "Portfolio",
            "Employment 🚀"
        ];

        let wordIndex = 0;
        let characterIndex = 0;
        let isDeleting = false;

        const typing = () => {
            const currentWord = words[wordIndex];

            if (isDeleting) {
                characterIndex--;
            } else {
                characterIndex++;
            }

            typingTarget.textContent = currentWord.slice(
                0,
                characterIndex
            );

            let delay = isDeleting ? 45 : 90;

            if (!isDeleting && characterIndex === currentWord.length) {
                isDeleting = true;
                delay = 1000;
            } else if (isDeleting && characterIndex === 0) {
                isDeleting = false;
                wordIndex = (wordIndex + 1) % words.length;
                delay = 300;
            }

            setTimeout(typing, delay);
        };

        typing();
    }

    /* =========================
       Header Scroll
    ========================= */

    const header = document.querySelector(
        ".header, header"
    );

    const updateHeader = () => {
        if (!header) return;

        header.classList.toggle(
            "active",
            window.scrollY > 30
        );

        header.classList.toggle(
            "scrolled",
            window.scrollY > 30
        );
    };

    updateHeader();
    window.addEventListener("scroll", updateHeader);

    /* =========================
       Scroll Progress
    ========================= */

    const progressBar = document.querySelector(
        ".progress-bar, .scroll-progress"
    );

    const updateProgress = () => {
        if (!progressBar) return;

        const scrollHeight =
            document.documentElement.scrollHeight -
            window.innerHeight;

        const progress =
            scrollHeight > 0
                ? (window.scrollY / scrollHeight) * 100
                : 0;

        progressBar.style.width = `${progress}%`;
    };

    updateProgress();
    window.addEventListener("scroll", updateProgress);

    /* =========================
       Smooth Scroll
    ========================= */

    document
        .querySelectorAll('a[href^="#"]')
        .forEach((anchor) => {
            anchor.addEventListener("click", (event) => {
                const href = anchor.getAttribute("href");

                if (!href || href === "#") return;

                const target = document.querySelector(href);

                if (!target) return;

                event.preventDefault();

                const headerHeight = header
                    ? header.offsetHeight
                    : 0;

                const targetPosition =
                    target.getBoundingClientRect().top +
                    window.scrollY -
                    headerHeight;

                window.scrollTo({
                    top: targetPosition,
                    behavior: "smooth"
                });

                closeMobileMenu();
            });
        });

    /* =========================
       Navigation Active
    ========================= */

    const sections = document.querySelectorAll(
        "main section[id], section[id]"
    );

    const navigationLinks = document.querySelectorAll(
        'nav a[href^="#"], .nav a[href^="#"]'
    );

    const updateActiveNavigation = () => {
        let currentSection = "";

        sections.forEach((section) => {
            const sectionTop =
                section.offsetTop - window.innerHeight * 0.35;

            if (window.scrollY >= sectionTop) {
                currentSection = section.id;
            }
        });

        navigationLinks.forEach((link) => {
            const href = link.getAttribute("href");

            link.classList.toggle(
                "active",
                href === `#${currentSection}`
            );
        });
    };

    updateActiveNavigation();
    window.addEventListener(
        "scroll",
        updateActiveNavigation
    );

    /* =========================
       Mobile Menu
    ========================= */

    const menuButton = document.querySelector(
        ".menu-toggle, .mobile-menu-button, .hamburger"
    );

    const navigation = document.querySelector(
        ".nav, .header__nav, nav"
    );

    const closeMobileMenu = () => {
        if (!menuButton || !navigation) return;

        menuButton.classList.remove("active");
        navigation.classList.remove("active");
        navigation.classList.remove("open");
        document.body.classList.remove("menu-open");

        menuButton.setAttribute(
            "aria-expanded",
            "false"
        );
    };

    if (menuButton && navigation) {
        menuButton.addEventListener("click", () => {
            const isOpen =
                navigation.classList.contains("active") ||
                navigation.classList.contains("open");

            menuButton.classList.toggle("active", !isOpen);
            navigation.classList.toggle("active", !isOpen);
            navigation.classList.toggle("open", !isOpen);
            document.body.classList.toggle(
                "menu-open",
                !isOpen
            );

            menuButton.setAttribute(
                "aria-expanded",
                String(!isOpen)
            );
        });
    }

    /* =========================
       Contact Form
    ========================= */

    const contactForm = document.querySelector(
        "#contactForm, .contact-form"
    );

    const formStatus = document.querySelector(
        "#formStatus, .contact-form__status"
    );

    if (contactForm) {
        contactForm.addEventListener(
            "submit",
            (event) => {
                event.preventDefault();

                const requiredFields =
                    contactForm.querySelectorAll(
                        "[required]"
                    );

                let isValid = true;

                requiredFields.forEach((field) => {
                    if (!field.value.trim()) {
                        isValid = false;
                        field.classList.add("error");
                    } else {
                        field.classList.remove("error");
                    }
                });

                if (!isValid) {
                    if (formStatus) {
                        formStatus.textContent =
                            "필수 항목을 모두 입력해주세요.";
                    }

                    return;
                }

                if (formStatus) {
                    formStatus.textContent =
                        "메시지가 확인되었습니다. 감사합니다.";
                }

                contactForm.reset();
            }
        );
    }

    /* =========================
       Footer Year
    ========================= */

    document
        .querySelectorAll(".year, [data-year]")
        .forEach((yearElement) => {
            yearElement.textContent =
                new Date().getFullYear();
        });

    /* =========================
       Resize
    ========================= */

    window.addEventListener("resize", () => {
        if (window.innerWidth > 768) {
            closeMobileMenu();
        }

        updateProgress();
    });
});

document.querySelectorAll(".year").forEach((year) => {
    year.textContent = new Date().getFullYear();
});