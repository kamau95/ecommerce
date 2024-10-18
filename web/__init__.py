from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, current_user
from os import path, getenv
from dotenv import load_dotenv

db = SQLAlchemy()
migrate = Migrate()  # Initialize Migrate without parameters
# Specify MySQL database name
DB_NAME = "SOKONI"

def create_app():
    load_dotenv()  # Load environment variables from .env file

    database_uri = getenv('DATABASE_URI')
    secret_key = getenv('SECRET_KEY')

    app = Flask(__name__)
    app.config['SECRET_KEY'] = secret_key
    # Update the SQLALCHEMY_DATABASE_URI for MySQL
    app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    migrate.init_app(app, db)  # Pass app and db here

    from .views import views
    from .auth import auth
    from .models import User

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    @app.errorhandler(404)  # Move this inside create_app
    def page_not_found(e):
        return render_template('404.html', user=current_user), 404

    return app


def add_sample_products():
    from .models import Product
    products = [
        Product(product_name="SONY OLED TELEVISION", category="electronics", price=899000, description="UHD 4K 3840 x 2160 OLED Panel, Google TV OS, 120 Hz Native Refresh Rate, Auto HDR Tone Mapping, ALLM & VRR, Google Assistant & Chromecast Built-In, Works with Alexa & Siri", photo="/static/img/1.avif"),
        Product(product_name="Electric Heaters", category="appliances", price=1300, description="Black in color, it uses 2 watts rating", photo="/static/img/2.avif"),
        Product(product_name="Hisense 43A6K 4K Smart LED TV", category="electronics", price=43899, description="Screen size: 43 inches, Dolby Vision HDR, Bluetooth Audio, Refresh rate: 60Hertz, Viewing Angle: 178°, Web browser: Odin", photo="/static/img/3.avif"),
        Product(product_name="Ultimate Ears Megaboom3", category="electronics", price=27000, description="Wireless Streaming via Bluetooth, 360° Sound, Up to 20 Hours of Playback, 2x 2″ Drivers & 4 Ohms Full Range Driver", photo="/static/img/5.avif"),
        Product(product_name="Von VHF182MLK Fan Heater", category="appliances", price=5489, description="Fan heater – with 2 heat settings 900W/1800W, Normal fan mode, Wide angle oscillation, Outer curved handle – Easy to carry and portable, PTC elements – overheat protection", photo="static/img/6.avif"),
        Product(product_name="Samsung Washing Machine", category="appliances", price=78000 , description="8KG Front load washing machine, 1200rpm, 12 washing programs (15-minute quick wash, Daily wash, Wool/Delicates, Hygiene steam, Colours, Bedding, Cotton, Cotton Eco, Synthetics, Rinse + Spin, Drain, Drum clean)", photo="/static/img/7.avif"),
        Product(product_name="Sony Speakers SRS XB100", category="electronics", price= 9995, description="Ultra-Compact & Portable Design, IP67-Rated Water & Dust Resistance, Sound Diffusion Processor for Big Sound, 1.8 Full-Range & Passive Radiator, Up to 16 Hours of Playback, Bluetooth 5.3 Compatible", photo="/static/img/8.avif"),
        Product(product_name="Table Top Dual Burner", category="appliances", price=4495 , description="2 Dual burners, Dual swirl burner. Enamel-coated pan support, 4 foldable ears., Auto ignition.", photo="/static/img/9.avif"),
        Product(product_name="Kenwood MOM45 Toaster Oven", category="appliances", price=17999 , description="1800W Interior light, 45ltr Capacity, Double glass door, Rotisserie Function, Convection Function", photo="/static/img/10.avif"),
        Product(product_name="JBL Wireless Microphone Set", category="electronics", price=22220 , description="Receiver & 2 Wireless Microphones, Plugs into Any 1/4, Play Setup, 6 Hours of Receiver Power", photo="/static/img/11.avif"),
        Product(product_name="Fan Heater", category="appliances", price=4369, description="""Fan Heater with 2 settings 1000W/ 2000W, The heater can be used as a Fan and heater, Tip-over safety switch – Switches off the heater once it falls, Outer curved handle – Easy to carry and portable.""", photo="/static/img/12.avif"),
        Product(product_name="Multi-Device Bluetooth Keyboard", category="electronics", price=14000 , description="Bluetooth LE & Logi Bolt Connectivity, Pairs with 3 Devices, Quiet, Low-Profile Keys, Compact, Portable Design, Dedicated Shortcut Keys, Includes AAA Batteries", photo="/static/img/13.avif"),
        Product(product_name="Vacuum Cleaner", category="appliances", price=18390 , description="1800W Max Power Delivers powerful suction for efficient cleaning, 2.5L Dust Box Capacity Holds more dirt before emptying, Suction Power > 20KPa Strong cleaning performance for removing stubborn dirt", photo="/static/img/14.avif"),
        Product(product_name="Oraimo Wireless Earbuds", category="electronics", price=4655 , description="Incredibly Powerful Bass, Power to Amaze You - Featuring HeavyBass™ exclusive algorithm", photo="/static/img/15.avif"),
        Product(product_name="Twin Tab Washing Machine", category="appliances", price=27600 , description="""Semi-automatic twin tub
Capacity – 8kgs, Free Water filtration device, 15minute wash timer, Air Dry function- for cleaner, dryer, and odor-free laundry, 2 Wash Program Selection""", photo="/static/img/16.avif"),
        Product(product_name="Samsung 75 QA75QN800CUXKE Neo-QLED TV - 8K", category="electronics", price=600100 , description="""Real 8K Resolution: See Details within the details, Quantum Ultra-fine contrast in 8K that brings out hidden details""", photo="/static/img/17.avif"),
        Product(product_name="Straightener Hair Brush", category="appliances", price=12000 , description="Keratin-infused ceramic coating for shiny, smooth, frizz-free hair, Silk ProCare to minimize heat damage on hair, ThermoProtect technology which maintains even temperature across the brush to prevent overheating", photo="/static/img/18.avif"),
        Product(product_name="Logitech H340 USB Headset", category="electronics", price= 4598, description="USB Connectivity with 6′ Cable, Plug & Play Design, Supports Clear Digital Audio, Lightweight & Flexible Headband, Works with Games, Music & Movies", photo="/static/img/19.avif"),
        Product(product_name="Easy Trim Hair Trimmer Recharge", category="appliances", price=7690 , description="Finest Precision Blades: Self-sharpening precision ground blades stay sharp longer ensuring you get professional-style haircuts effortlessly over a long period of use", photo="/static/img/20.avif")
    ]
    db.session.bulk_save_objects(products)
    db.session.commit()

def create_database(app):
    with app.app_context():
        db.create_all()  # Create all tables if they don't exist
        from .models import Product
        
        # Check if there are any products in the database
        if Product.query.first() is None:
            add_sample_products()
            print('Sample products added!')
        print('Database setup completed!')
