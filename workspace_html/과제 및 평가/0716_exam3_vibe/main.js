"use strict";

document.addEventListener("DOMContentLoaded", () => {
    /* ==================================================
       1. Element Selectors
    ================================================== */

    const body = document.body;
    const header = document.querySelector(".header");
    const nav = document.querySelector(".nav");
    const menuToggle = document.querySelector(".menu-toggle");

    const navLinks = document.querySelectorAll(".nav__link");
    const sectionLinks = document.querySelectorAll('a[href^="#"]');
    const sections = document.querySelectorAll("main section[id]");

    const progressBar = document.querySelector(
        ".scroll-progress__bar"
    );

    const revealElements = document.querySelectorAll(".reveal");

    const accordionButtons = document.querySelectorAll(
        ".accordion-button"
    );

    const footerHeadings = document.querySelectorAll(
        ".footer__heading"
    );

    const contactForm = document.querySelector("#contactForm");
    const formStatus = document.querySelector("#formStatus");

    const yearElements = document.querySelectorAll(".year");


    /* ==================================================
       2. Utility Functions
    ================================================== */

    const isMobileNavigation = () => {
        return window.innerWidth <= 900;
    };

    const isMobileFooter = () => {
        return window.innerWidth <= 640;
    };

    const getHeaderHeight = () => {
        return header ? header.offsetHeight : 0;
    };


    /* ==================================================
       3. Mobile Navigation
    ================================================== */

    const openMobileMenu = () => {
        if (!nav || !menuToggle || !header) return;

        nav.classList.add("open");
        menuToggle.classList.add("active");
        header.classList.add("nav-open");
        body.classList.add("menu-open");

        menuToggle.setAttribute("aria-expanded", "true");
        menuToggle.setAttribute("aria-label", "메뉴 닫기");
    };

    const closeMobileMenu = () => {
        if (!nav || !menuToggle || !header) return;

        nav.classList.remove("open");
        menuToggle.classList.remove("active");
        header.classList.remove("nav-open");
        body.classList.remove("menu-open");

        menuToggle.setAttribute("aria-expanded", "false");
        menuToggle.setAttribute("aria-label", "메뉴 열기");
    };

    const toggleMobileMenu = () => {
        if (!nav) return;

        const isOpen = nav.classList.contains("open");

        if (isOpen) {
            closeMobileMenu();
        } else {
            openMobileMenu();
        }
    };

    if (menuToggle) {
        menuToggle.addEventListener("click", toggleMobileMenu);
    }

    if (nav) {
        nav.addEventListener("click", (event) => {
            if (
                event.target === nav &&
                isMobileNavigation()
            ) {
                closeMobileMenu();
            }
        });
    }

    document.addEventListener("keydown", (event) => {
        if (
            event.key === "Escape" &&
            nav?.classList.contains("open")
        ) {
            closeMobileMenu();
            menuToggle?.focus();
        }
    });


    /* ==================================================
       4. Smooth Scroll
    ================================================== */

    sectionLinks.forEach((link) => {
        link.addEventListener("click", (event) => {
            const href = link.getAttribute("href");

            if (!href || href === "#") {
                event.preventDefault();
                return;
            }

            let target;

            try {
                target = document.querySelector(href);
            } catch (error) {
                return;
            }

            if (!target) return;

            event.preventDefault();

            const targetTop =
                target.getBoundingClientRect().top +
                window.scrollY -
                getHeaderHeight();

            window.scrollTo({
                top: Math.max(targetTop, 0),
                behavior: "smooth"
            });

            if (isMobileNavigation()) {
                closeMobileMenu();
            }
        });
    });


    /* ==================================================
       5. Header Scroll State
    ================================================== */

    const updateHeader = () => {
        if (!header) return;

        header.classList.toggle(
            "scrolled",
            window.scrollY > 20
        );
    };


    /* ==================================================
       6. Scroll Progress
    ================================================== */

    const updateScrollProgress = () => {
        if (!progressBar) return;

        const documentHeight =
            document.documentElement.scrollHeight -
            window.innerHeight;

        const scrollPercent =
            documentHeight > 0
                ? (window.scrollY / documentHeight) * 100
                : 0;

        progressBar.style.width =
            `${Math.min(Math.max(scrollPercent, 0), 100)}%`;
    };


    /* ==================================================
       7. Active Navigation
    ================================================== */

    const updateActiveNavigation = () => {
        if (!sections.length || !navLinks.length) return;

        const scrollPosition =
            window.scrollY +
            getHeaderHeight() +
            window.innerHeight * 0.25;

        let currentSectionId = sections[0].id;

        sections.forEach((section) => {
            if (scrollPosition >= section.offsetTop) {
                currentSectionId = section.id;
            }
        });

        navLinks.forEach((link) => {
            const href = link.getAttribute("href");

            link.classList.toggle(
                "active",
                href === `#${currentSectionId}`
            );
        });
    };


    /* ==================================================
       8. Reveal Animation
    ================================================== */

    const showAllRevealElements = () => {
        revealElements.forEach((element) => {
            element.classList.add("show");
        });
    };

    if (
        "IntersectionObserver" in window &&
        !window.matchMedia(
            "(prefers-reduced-motion: reduce)"
        ).matches
    ) {
        const revealObserver = new IntersectionObserver(
            (entries, observer) => {
                entries.forEach((entry) => {
                    if (!entry.isIntersecting) return;

                    entry.target.classList.add("show");
                    observer.unobserve(entry.target);
                });
            },
            {
                threshold: 0.12,
                rootMargin: "0px 0px -50px 0px"
            }
        );

        revealElements.forEach((element) => {
            revealObserver.observe(element);
        });

        /*
         * 첫 화면 요소가 observer 계산 전에
         * 숨겨진 채 남는 상황을 방지한다.
         */
        window.setTimeout(() => {
            revealElements.forEach((element) => {
                const rect = element.getBoundingClientRect();

                if (rect.top < window.innerHeight) {
                    element.classList.add("show");
                }
            });
        }, 100);
    } else {
        showAllRevealElements();
    }


    /* ==================================================
       9. General Accordion
       Courses / FAQ
    ================================================== */

    const closeAccordionItem = (button) => {
        const item = button.closest(".accordion-item");
        const panel = item?.querySelector(".accordion-panel");

        if (!panel) return;

        button.setAttribute("aria-expanded", "false");
        panel.hidden = true;
        item.classList.remove("open");
    };

    const openAccordionItem = (button) => {
        const item = button.closest(".accordion-item");
        const panel = item?.querySelector(".accordion-panel");

        if (!panel) return;

        button.setAttribute("aria-expanded", "true");
        panel.hidden = false;
        item.classList.add("open");
    };

    accordionButtons.forEach((button) => {
        button.addEventListener("click", () => {
            const item = button.closest(".accordion-item");
            const accordionContainer =
                item?.parentElement;

            if (!item || !accordionContainer) return;

            const isOpen =
                button.getAttribute("aria-expanded") === "true";

            /*
             * 같은 아코디언 그룹에서는 하나만 열리도록 한다.
             */
            const siblingButtons =
                accordionContainer.querySelectorAll(
                    ":scope > .accordion-item .accordion-button"
                );

            siblingButtons.forEach((siblingButton) => {
                if (siblingButton !== button) {
                    closeAccordionItem(siblingButton);
                }
            });

            if (isOpen) {
                closeAccordionItem(button);
            } else {
                openAccordionItem(button);
            }
        });
    });


    /* ==================================================
       10. Mobile Footer Accordion
    ================================================== */

    const closeFooterSection = (heading) => {
        const column = heading.closest(".footer__column");

        if (!column) return;

        heading.setAttribute("aria-expanded", "false");
        column.classList.remove("open");
    };

    const openFooterSection = (heading) => {
        const column = heading.closest(".footer__column");

        if (!column) return;

        heading.setAttribute("aria-expanded", "true");
        column.classList.add("open");
    };

    footerHeadings.forEach((heading) => {
        heading.addEventListener("click", () => {
            if (!isMobileFooter()) return;

            const isOpen =
                heading.getAttribute("aria-expanded") === "true";

            footerHeadings.forEach((otherHeading) => {
                if (otherHeading !== heading) {
                    closeFooterSection(otherHeading);
                }
            });

            if (isOpen) {
                closeFooterSection(heading);
            } else {
                openFooterSection(heading);
            }
        });
    });

    const resetFooterAccordion = () => {
        if (isMobileFooter()) {
            footerHeadings.forEach((heading) => {
                closeFooterSection(heading);
            });

            return;
        }

        footerHeadings.forEach((heading) => {
            const column = heading.closest(".footer__column");

            heading.setAttribute("aria-expanded", "true");
            column?.classList.remove("open");
        });
    };


    /* ==================================================
       11. Contact Form Validation
    ================================================== */

    const showFormStatus = (message, type = "default") => {
        if (!formStatus) return;

        formStatus.textContent = message;

        formStatus.classList.remove(
            "success",
            "error"
        );

        if (type !== "default") {
            formStatus.classList.add(type);
        }
    };

    const clearFieldError = (field) => {
        field.classList.remove("error");
        field.removeAttribute("aria-invalid");
    };

    const setFieldError = (field) => {
        field.classList.add("error");
        field.setAttribute("aria-invalid", "true");
    };

    const validateContactForm = () => {
        if (!contactForm) return false;

        const requiredFields =
            contactForm.querySelectorAll("[required]");

        let firstInvalidField = null;
        let isValid = true;

        requiredFields.forEach((field) => {
            clearFieldError(field);

            let fieldIsValid = true;

            if (field.type === "checkbox") {
                fieldIsValid = field.checked;
            } else {
                fieldIsValid = field.value.trim() !== "";
            }

            if (
                field.type === "tel" &&
                field.value.trim()
            ) {
                const phonePattern =
                    /^[0-9\s\-()+]{9,20}$/;

                fieldIsValid =
                    phonePattern.test(field.value.trim());
            }

            if (!fieldIsValid) {
                isValid = false;
                setFieldError(field);

                if (!firstInvalidField) {
                    firstInvalidField = field;
                }
            }
        });

        if (firstInvalidField) {
            firstInvalidField.focus();
        }

        return isValid;
    };

    if (contactForm) {
        contactForm.addEventListener("input", (event) => {
            const field = event.target;

            if (
                field instanceof HTMLInputElement ||
                field instanceof HTMLSelectElement ||
                field instanceof HTMLTextAreaElement
            ) {
                clearFieldError(field);
                showFormStatus("");
            }
        });

        contactForm.addEventListener("change", (event) => {
            const field = event.target;

            if (
                field instanceof HTMLInputElement ||
                field instanceof HTMLSelectElement
            ) {
                clearFieldError(field);
            }
        });

        contactForm.addEventListener("submit", (event) => {
            event.preventDefault();

            const isValid = validateContactForm();

            if (!isValid) {
                showFormStatus(
                    "필수 항목을 정확하게 입력해주세요.",
                    "error"
                );

                return;
            }

            /*
             * 현재는 서버 전송 기능이 연결되지 않은
             * 프론트엔드 예시 폼이다.
             */
            showFormStatus(
                "상담 신청이 완료되었습니다. 담당자가 확인 후 연락드리겠습니다.",
                "success"
            );

            contactForm.reset();

            contactForm
                .querySelectorAll(".error")
                .forEach((field) => {
                    clearFieldError(field);
                });
        });
    }


    /* ==================================================
       12. Footer Year
    ================================================== */

    const currentYear = new Date().getFullYear();

    yearElements.forEach((element) => {
        element.textContent = currentYear;
    });


    /* ==================================================
       13. Scroll Event Optimization
    ================================================== */

    let scrollTicking = false;

    const handleScroll = () => {
        if (scrollTicking) return;

        scrollTicking = true;

        window.requestAnimationFrame(() => {
            updateHeader();
            updateScrollProgress();
            updateActiveNavigation();

            scrollTicking = false;
        });
    };

    window.addEventListener(
        "scroll",
        handleScroll,
        { passive: true }
    );


    /* ==================================================
       14. Resize
    ================================================== */

    let resizeTimer;

    window.addEventListener("resize", () => {
        window.clearTimeout(resizeTimer);

        resizeTimer = window.setTimeout(() => {
            if (!isMobileNavigation()) {
                closeMobileMenu();
            }

            resetFooterAccordion();
            updateScrollProgress();
            updateActiveNavigation();
        }, 150);
    });


    /* ==================================================
       15. Initial Execution
    ================================================== */

    updateHeader();
    updateScrollProgress();
    updateActiveNavigation();
    resetFooterAccordion();
});