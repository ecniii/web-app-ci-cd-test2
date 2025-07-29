from flask import Flask
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP Requests')

@app.route('/')
def home():
    REQUEST_COUNT.inc()
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>KMC E-Commerce Store</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: #f8f9fa;
                color: #333;
            }
            
            .navbar {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                padding: 1rem 0;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                position: sticky;
                top: 0;
                z-index: 1000;
            }
            
            .nav-container {
                max-width: 1200px;
                margin: 0 auto;
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 0 2rem;
            }
            
            .logo {
                color: white;
                font-size: 1.5rem;
                font-weight: bold;
            }
            
            .nav-menu {
                display: flex;
                gap: 2rem;
                list-style: none;
            }
            
            .nav-menu li a {
                color: white;
                text-decoration: none;
                font-weight: 500;
                transition: color 0.3s;
            }
            
            .nav-menu li a:hover {
                color: #ffd700;
            }
            
            .cart-icon {
                position: relative;
                cursor: pointer;
            }
            
            .cart-count {
                position: absolute;
                top: -8px;
                right: -8px;
                background: #ff4757;
                color: white;
                border-radius: 50%;
                width: 20px;
                height: 20px;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 0.8rem;
            }
            
            .hero {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                text-align: center;
                padding: 4rem 2rem;
            }
            
            .hero h1 {
                font-size: 3rem;
                margin-bottom: 1rem;
            }
            
            .hero p {
                font-size: 1.2rem;
                margin-bottom: 2rem;
            }
            
            .cta-button {
                background: #ffd700;
                color: #333;
                padding: 1rem 2rem;
                border: none;
                border-radius: 5px;
                font-size: 1.1rem;
                font-weight: bold;
                cursor: pointer;
                transition: transform 0.3s;
            }
            
            .cta-button:hover {
                transform: translateY(-2px);
            }
            
            .container {
                max-width: 1200px;
                margin: 0 auto;
                padding: 2rem;
            }
            
            .section-title {
                text-align: center;
                font-size: 2.5rem;
                margin-bottom: 3rem;
                color: #333;
            }
            
            .products-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
                gap: 2rem;
                margin-bottom: 4rem;
            }
            
            .product-card {
                background: white;
                border-radius: 10px;
                overflow: hidden;
                box-shadow: 0 4px 15px rgba(0,0,0,0.1);
                transition: transform 0.3s;
            }
            
            .product-card:hover {
                transform: translateY(-5px);
            }
            
            .product-image {
                width: 100%;
                height: 200px;
                background: linear-gradient(45deg, #667eea, #764ba2);
                display: flex;
                align-items: center;
                justify-content: center;
                color: white;
                font-size: 3rem;
            }
            
            .product-info {
                padding: 1.5rem;
            }
            
            .product-title {
                font-size: 1.2rem;
                font-weight: bold;
                margin-bottom: 0.5rem;
            }
            
            .product-price {
                font-size: 1.5rem;
                color: #667eea;
                font-weight: bold;
                margin-bottom: 1rem;
            }
            
            .add-to-cart {
                background: #667eea;
                color: white;
                border: none;
                padding: 0.8rem 1.5rem;
                border-radius: 5px;
                cursor: pointer;
                width: 100%;
                font-weight: bold;
                transition: background 0.3s;
            }
            
            .add-to-cart:hover {
                background: #5a6fd8;
            }
            
            .features {
                background: white;
                padding: 4rem 2rem;
                margin: 2rem 0;
            }
            
            .features-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 2rem;
                max-width: 1200px;
                margin: 0 auto;
            }
            
            .feature {
                text-align: center;
                padding: 2rem;
            }
            
            .feature-icon {
                font-size: 3rem;
                margin-bottom: 1rem;
                color: #667eea;
            }
            
            .footer {
                background: #333;
                color: white;
                text-align: center;
                padding: 2rem;
                margin-top: 4rem;
            }
            
            @media (max-width: 768px) {
                .nav-container {
                    flex-direction: column;
                    gap: 1rem;
                }
                
                .hero h1 {
                    font-size: 2rem;
                }
                
                .products-grid {
                    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                }
            }
        </style>
    </head>
    <body>
        <nav class="navbar">
            <div class="nav-container">
                <div class="logo">KMC Store</div>
                <ul class="nav-menu">
                    <li><a href="#home">Home</a></li>
                    <li><a href="#products">Products</a></li>
                    <li><a href="#about">About</a></li>
                    <li><a href="#contact">Contact</a></li>
                </ul>
                <div class="cart-icon">
                    🛒
                    <span class="cart-count">0</span>
                </div>
            </div>
        </nav>
        
        <section class="hero" id="home">
            <h1>Welcome to KMC E-Commerce</h1>
            <p>Discover amazing products at unbeatable prices</p>
            <button class="cta-button">Shop Now</button>
        </section>
        
        <div class="container">
            <h2 class="section-title" id="products">Featured Products</h2>
            <div class="products-grid">
                <div class="product-card">
                    <div class="product-image">📱</div>
                    <div class="product-info">
                        <div class="product-title">Smartphone Pro</div>
                        <div class="product-price">$599.99</div>
                        <button class="add-to-cart">Add to Cart</button>
                    </div>
                </div>
                
                <div class="product-card">
                    <div class="product-image">💻</div>
                    <div class="product-info">
                        <div class="product-title">Laptop Ultra</div>
                        <div class="product-price">$1,299.99</div>
                        <button class="add-to-cart">Add to Cart</button>
                    </div>
                </div>
                
                <div class="product-card">
                    <div class="product-image">🎧</div>
                    <div class="product-info">
                        <div class="product-title">Wireless Headphones</div>
                        <div class="product-price">$199.99</div>
                        <button class="add-to-cart">Add to Cart</button>
                    </div>
                </div>
                
                <div class="product-card">
                    <div class="product-image">⌚</div>
                    <div class="product-info">
                        <div class="product-title">Smart Watch</div>
                        <div class="product-price">$349.99</div>
                        <button class="add-to-cart">Add to Cart</button>
                    </div>
                </div>
                
                <div class="product-card">
                    <div class="product-image">📷</div>
                    <div class="product-info">
                        <div class="product-title">Digital Camera</div>
                        <div class="product-price">$799.99</div>
                        <button class="add-to-cart">Add to Cart</button>
                    </div>
                </div>
                
                <div class="product-card">
                    <div class="product-image">🎮</div>
                    <div class="product-info">
                        <div class="product-title">Gaming Console</div>
                        <div class="product-price">$499.99</div>
                        <button class="add-to-cart">Add to Cart</button>
                    </div>
                </div>
            </div>
        </div>
        
        <section class="features">
            <div class="features-grid">
                <div class="feature">
                    <div class="feature-icon">🚚</div>
                    <h3>Free Shipping</h3>
                    <p>Free shipping on orders over $50</p>
                </div>
                <div class="feature">
                    <div class="feature-icon">🔄</div>
                    <h3>Easy Returns</h3>
                    <p>30-day return policy</p>
                </div>
                <div class="feature">
                    <div class="feature-icon">🔒</div>
                    <h3>Secure Payment</h3>
                    <p>100% secure payment processing</p>
                </div>
                <div class="feature">
                    <div class="feature-icon">📞</div>
                    <h3>24/7 Support</h3>
                    <p>Round the clock customer support</p>
                </div>
            </div>
        </section>
        
        <footer class="footer">
            <p>&copy; 2024 KMC E-Commerce Store. All rights reserved.</p>
        </footer>
        
        <script>
            // Simple cart functionality
            let cartCount = 0;
            const cartCountElement = document.querySelector('.cart-count');
            const addToCartButtons = document.querySelectorAll('.add-to-cart');
            
            addToCartButtons.forEach(button => {
                button.addEventListener('click', () => {
                    cartCount++;
                    cartCountElement.textContent = cartCount;
                    button.textContent = 'Added!';
                    button.style.background = '#28a745';
                    
                    setTimeout(() => {
                        button.textContent = 'Add to Cart';
                        button.style.background = '#667eea';
                    }, 1000);
                });
            });
            
            // Smooth scrolling for navigation links
            document.querySelectorAll('a[href^="#"]').forEach(anchor => {
                anchor.addEventListener('click', function (e) {
                    e.preventDefault();
                    const target = document.querySelector(this.getAttribute('href'));
                    if (target) {
                        target.scrollIntoView({
                            behavior: 'smooth'
                        });
                    }
                });
            });
        </script>
    </body>
    </html>
    '''

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
