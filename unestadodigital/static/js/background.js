document.addEventListener('DOMContentLoaded', function () {
    const canvas = document.createElement("canvas");
    document.getElementById("background-container").appendChild(canvas);
    const ctx = canvas.getContext("2d");

    function resizeCanvas() {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    }

    window.addEventListener("resize", resizeCanvas);

    resizeCanvas();

    class Particle {
        constructor() {
            this.x = Math.random() * canvas.width;
            this.y = Math.random() * canvas.height;
            this.size = Math.random() * 5 + 1;
            this.speedX = Math.random() * 3 - 1.5;
            this.speedY = Math.random() * 3 - 1.5;
        }

        update() {
            this.x += this.speedX;
            this.y += this.speedY;

            if (this.x > canvas.width + this.size || this.x < -this.size || this.y > canvas.height + this.size || this.y < -this.size) {
                this.x = Math.random() * canvas.width;
                this.y = Math.random() * canvas.height;
            }

            if (this.size > 0.2) this.size -= 0.1;
        }

        draw() {
            ctx.fillStyle = "rgba(150, 179, 255, 0.3)";
            ctx.strokeStyle = "rgba(1, 75, 160, 0.3)";
            ctx.lineWidth = 2;
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
            ctx.fill();
            ctx.stroke();
        }
    }

    const particles = [];

    function init() {
        for (let i = 0; i < 200; i++) {
            particles.push(new Particle());
        }
    }

    init();

    function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        for (let i = 0; i < particles.length; i++) {
            particles[i].update();
            particles[i].draw();
        }

        connect();
        requestAnimationFrame(animate);
    }

    animate();

    function connect() {
        let opacityValue = 1;
        for (let a = 0; a < particles.length; a++) {
            for (let b = a; b < particles.length; b++) {
                const distance = Math.sqrt(
                    (particles[a].x - particles[b].x) ** 2 +
                    (particles[a].y - particles[b].y) ** 2
                );

                if (distance < 100) {
                    opacityValue = 1 - distance / 100;
                    ctx.strokeStyle = `rgba(143, 0, 255,${opacityValue})`;
                    ctx.lineWidth = 0.1;
                    ctx.beginPath();
                    ctx.moveTo(particles[a].x, particles[a].y);
                    ctx.lineTo(particles[b].x, particles[b].y);
                    ctx.stroke();
                }
            }
        }
    }
});