gsap.registerPlugin(ScrollTrigger);

gsap.from(".hero-content h1", {
    duration: 1.5,
    y: 100,
    opacity: 0,
    ease: "power4.out",
    delay: 0.5
});

gsap.from(".hero-content p", {
    duration: 1.5,
    y: 50,
    opacity: 0,
    ease: "power4.out",
    delay: 1
});

gsap.from(".hero-content .cta-button", {
    duration: 1,
    scale: 0,
    opacity: 0,
    ease: "back.out(1.7)",
    delay: 1.5
});

gsap.from(".hero-image img", {
    duration: 2,
    x: 100,
    opacity: 0,
    ease: "power4.out",
    delay: 0.5
});

gsap.from(".navbar", {
    duration: 1,
    y: -100,
    opacity: 0,
    ease: "power4.out"
});

gsap.utils.toArray(".feature-card").forEach((card, i) => {
    gsap.from(card, {
        scrollTrigger: {
            trigger: card,
            start: "top bottom-=100",
            toggleActions: "play none none reverse"
        },
        duration: 1,
        y: 100,
        opacity: 0,
        ease: "power4.out",
        delay: i * 0.2
    });
});

gsap.utils.toArray(".feature-card i").forEach((icon, i) => {
    gsap.from(icon, {
        scrollTrigger: {
            trigger: icon,
            start: "top bottom-=100",
            toggleActions: "play none none reverse"
        },
        duration: 1,
        scale: 0,
        rotation: 360,
        ease: "back.out(1.7)",
        delay: i * 0.2
    });
});

gsap.from("#about", {
    scrollTrigger: {
        trigger: "#about",
        start: "top bottom-=100",
        toggleActions: "play none none reverse"
    },
    duration: 1.5,
    y: 100,
    opacity: 0,
    ease: "power4.out"
});

gsap.from("footer", {
    scrollTrigger: {
        trigger: "footer",
        start: "top bottom-=100",
        toggleActions: "play none none reverse"
    },
    duration: 1,
    y: 50,
    opacity: 0,
    ease: "power4.out"
});

gsap.to(".hero-image img", {
    scrollTrigger: {
        trigger: ".hero",
        start: "top top",
        end: "bottom top",
        scrub: true
    },
    y: 100,
    scale: 1.1,
    ease: "none"
});

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const targetId = this.getAttribute('href');
        if (targetId === '#') return;
        
        const targetElement = document.querySelector(targetId);
        if (targetElement) {
            targetElement.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

const navbar = document.querySelector('.navbar');
let lastScroll = 0;

window.addEventListener('scroll', () => {
    const currentScroll = window.pageYOffset;
    
    if (currentScroll <= 0) {
        navbar.classList.remove('scroll-up');
        return;
    }
    
    if (currentScroll > lastScroll && !navbar.classList.contains('scroll-down')) {
        navbar.classList.remove('scroll-up');
        navbar.classList.add('scroll-down');
    } else if (currentScroll < lastScroll && navbar.classList.contains('scroll-down')) {
        navbar.classList.remove('scroll-down');
        navbar.classList.add('scroll-up');
    }
    lastScroll = currentScroll;
});

document.addEventListener('DOMContentLoaded', () => {
    const observerOptions = {
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate');
            }
        });
    }, observerOptions);

    document.querySelectorAll('.feature-card').forEach(card => {
        observer.observe(card);
    });

    const heroContent = document.querySelector('.hero-content');
    if (heroContent) {
        heroContent.classList.add('animate');
    }
});

gsap.from(".team h2", {
    scrollTrigger: {
        trigger: ".team",
        start: "top bottom-=100",
        toggleActions: "play none none reverse"
    },
    duration: 1,
    y: 50,
    opacity: 0,
    ease: "power4.out"
});

gsap.utils.toArray(".team-member").forEach((member, i) => {
    gsap.from(member, {
        scrollTrigger: {
            trigger: member,
            start: "top bottom-=100",
            toggleActions: "play none none reverse"
        },
        duration: 1,
        y: 100,
        opacity: 0,
        ease: "power4.out",
        delay: i * 0.2
    });

    gsap.from(member.querySelector(".member-icon"), {
        scrollTrigger: {
            trigger: member,
            start: "top bottom-=100",
            toggleActions: "play none none reverse"
        },
        duration: 1,
        scale: 0,
        rotation: 360,
        ease: "back.out(1.7)",
        delay: i * 0.2
    });
});

if (window.location.pathname.includes('features.html')) {
    gsap.from(".features-hero h1", {
        duration: 1.5,
        y: 100,
        opacity: 0,
        ease: "power4.out",
        delay: 0.5
    });

    gsap.from(".features-hero p", {
        duration: 1.5,
        y: 50,
        opacity: 0,
        ease: "power4.out",
        delay: 1
    });
    gsap.utils.toArray(".algorithm-card").forEach((card, i) => {
        gsap.from(card, {
            scrollTrigger: {
                trigger: card,
                start: "top bottom-=100",
                toggleActions: "play none none reverse"
            },
            duration: 1,
            y: 100,
            opacity: 0,
            ease: "power4.out",
            delay: i * 0.2
        });
    });
} 