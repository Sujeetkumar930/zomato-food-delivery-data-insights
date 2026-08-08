import streamlit as st
import pandas as pd
from db import Database

st.set_page_config(
    page_title="Zomato Dashboard",
    page_icon="🍽️",
    layout="wide"
)

# Connect Database
db = Database()

# Title
st.title("🍽️ Zomato - Food Delivery Data Insights Using Python and Sql")

# Sidebar
menu = st.sidebar.selectbox(
    "Select an Option",
    [
        "Home",
        "📊 Dashboard Overview",
        "🍽 Restaurant Analytics",
        "👥 Customer Analytics",
        "🛒 Order Analytics",
        "🛵 Delivery Person Analytics",
        "🚚 Delivery Analytics",
        "Restaurants",
        "Customers",
        "Orders",
        "Delivery Persons",
        "Deliveries",
        "Adding New Customer",
        "Add Restaurants",
        "Add Order",
        "Add Delivery Person",
        "Add Delivery",
        "Update Customer",
        "Update Restaurant",
        "Update Order",
        "Update Delivery",
        "Delete Customer",
        "Delete Order",
        "Delete Delivery",
        "Delete Restaurant",
        "Search Delivery",
        "Search Order",
    ]
)

# Home
if menu == "Home":
    
    st.success("Database Connected Successfully!")
    # Count records
    restaurant_count = db.fetch_data("SELECT COUNT(*) FROM restaurants")[0][0]
    customer_count = db.fetch_data("SELECT COUNT(*) FROM customers")[0][0]
    order_count = db.fetch_data("SELECT COUNT(*) FROM orders")[0][0]
    delivery_person_count = db.fetch_data("SELECT COUNT(*) FROM delivery_persons")[0][0]
    delivery_count = db.fetch_data("SELECT COUNT(*) FROM deliveries")[0][0]
    
    st.header("📊 Dashboard")
    
    st.subheader("🍽 Zomato Database Management System")

    st.markdown("""
    Welcome to the **Zomato Analytics Dashboard**.

    This application allows users to:

    - ✔ Manage Restaurants
    - ✔ Manage Customers
    - ✔ Manage Orders
    - ✔ Manage Deliveries
    - ✔ View Interactive Analytics
    - ✔ Perform CRUD Operations

    ### 🛠 Technology Used
    - 🐍 Python
    - 🎨 Streamlit
    - 🗄 MySQL

    ### 👨‍💻 Developer
    **Sujeet Kumar**
    """)

    st.divider()
    
    
# KPI Cards
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.metric("🍽️ Restaurants", restaurant_count)
        
        st.divider()
    with col2:
        st.metric("👥 Customers", customer_count)
        st.divider()
    with col3:
        st.metric("🛒 Orders", order_count)
        st.divider()
    with col4:
        st.metric("🛵 Delivery Persons", delivery_person_count)
        st.divider()
    with col5:
        st.metric("📦 Deliveries", delivery_count)
        st.divider()
        
        

    
        
        

        
        
        
        
   
        
        

elif menu == "📊 Dashboard Overview":
    st.header("📊 Dashboard Overview")
    
        # ================= Row 1 =================
    chart1, chart2 = st.columns(2)

    with chart1:
        st.subheader("📈 Orders by Status")

        status = db.fetch_data("""
            SELECT status, COUNT(*)
            FROM orders
            GROUP BY status
        """)

        status_df = pd.DataFrame(
            status,
            columns=["Status", "Count"]
        )

        st.bar_chart(status_df.set_index("Status"))

    with chart2:
        st.subheader("⭐ Top 10 Restaurants by Rating")

        rating = db.fetch_data("""
            SELECT name, rating
            FROM restaurants
            ORDER BY rating DESC
            LIMIT 10
        """)

        rating_df = pd.DataFrame(
            rating,
            columns=["Restaurant", "Rating"]
        )

        st.bar_chart(rating_df.set_index("Restaurant"))

    st.divider()

    # ================= Row 2 =================
    chart3, chart4 = st.columns(2)

    with chart3:
        st.subheader("🚚 Delivery Status")

        delivery = db.fetch_data("""
            SELECT delivery_status, COUNT(*)
            FROM deliveries
            GROUP BY delivery_status
        """)

        delivery_df = pd.DataFrame(
            delivery,
            columns=["Status", "Count"]
        )

        st.bar_chart(delivery_df.set_index("Status"))

    with chart4:
        st.subheader("👤 Top 10 Customers")

        customers = db.fetch_data("""
            SELECT
                c.name,
                SUM(o.total_amount) AS total_spent
            FROM customers c
            JOIN orders o
            ON c.customer_id = o.customer_id
            GROUP BY c.customer_id, c.name
            ORDER BY total_spent DESC
            LIMIT 10
        """)

        customer_df = pd.DataFrame(
            customers,
            columns=["Customer", "Total Spent"]
        )

        st.bar_chart(customer_df.set_index("Customer"))

    st.divider()

    # ================= Row 3 =================
    chart5, chart6 = st.columns(2)

    with chart5:
        st.subheader("🏆 Top Delivery Persons")

        delivery_persons = db.fetch_data("""
            SELECT
                dp.name,
                COUNT(d.delivery_id) AS total_deliveries
            FROM delivery_persons dp
            JOIN deliveries d
            ON dp.delivery_person_id = d.delivery_person_id
            GROUP BY dp.delivery_person_id, dp.name
            ORDER BY total_deliveries DESC
            LIMIT 10
        """)

        delivery_person_df = pd.DataFrame(
            delivery_persons,
            columns=["Delivery Person", "Deliveries"]
        )

        st.bar_chart(delivery_person_df.set_index("Delivery Person"))
        
elif menu == "🍽 Restaurant Analytics":
    st.header("🍽 Restaurant Analytics")
    
        # ================= Row 1 =================
    chart1, chart2 = st.columns(2)

    with chart1:
        st.subheader("🍕 Restaurant Cuisine Types")

        cuisines = db.fetch_data("""
            SELECT cuisine_type,
                   COUNT(*) AS total_restaurants
            FROM restaurants
            GROUP BY cuisine_type
            ORDER BY total_restaurants DESC
        """)

        cuisine_df = pd.DataFrame(
            cuisines,
            columns=["Cuisine", "Restaurants"]
        )

        st.bar_chart(cuisine_df.set_index("Cuisine"))

    with chart2:
        st.subheader("📍 Restaurant Locations")

        locations = db.fetch_data("""
            SELECT location,
                   COUNT(*) AS total_restaurants
            FROM restaurants
            GROUP BY location
            ORDER BY total_restaurants DESC
        """)

        location_df = pd.DataFrame(
            locations,
            columns=["Location", "Restaurants"]
        )

        st.bar_chart(location_df.set_index("Location"))

    st.divider()

    # ================= Row 2 =================
    chart3, chart4 = st.columns(2)

    with chart3:
        st.subheader("⭐ Restaurant Rating Distribution")

        ratings = db.fetch_data("""
            SELECT rating,
                   COUNT(*) AS total_restaurants
            FROM restaurants
            GROUP BY rating
            ORDER BY rating
        """)

        rating_df = pd.DataFrame(
            ratings,
            columns=["Rating", "Restaurants"]
        )

        st.bar_chart(rating_df.set_index("Rating"))

    with chart4:
        st.subheader("🏆 Top Restaurants by Orders")

        top_restaurants = db.fetch_data("""
            SELECT name,
                   total_orders
            FROM restaurants
            ORDER BY total_orders DESC
            LIMIT 10
        """)

        top_restaurants_df = pd.DataFrame(
            top_restaurants,
            columns=["Restaurant", "Orders"]
        )

        st.bar_chart(top_restaurants_df.set_index("Restaurant"))

    st.divider()

    # ================= Row 3 =================
    chart5, chart6 = st.columns(2)

    with chart5:
        st.subheader("⏱ Average Delivery Time")

        delivery_time = db.fetch_data("""
            SELECT name,
                   average_delivery_time
            FROM restaurants
            ORDER BY average_delivery_time
        """)

        delivery_time_df = pd.DataFrame(
            delivery_time,
            columns=["Restaurant", "Delivery Time (min)"]
        )

        st.bar_chart(delivery_time_df.set_index("Restaurant"))

    with chart6:
        st.subheader("✅ Active vs Inactive Restaurants")
        active = db.fetch_data("""
            SELECT is_active,
                   COUNT(*) AS total
            FROM restaurants
            GROUP BY is_active
        """)

        active_df = pd.DataFrame(
            active,
            columns=["Status", "Restaurants"]
        )

        active_df["Status"] = active_df["Status"].replace({
            1: "Active",
            0: "Inactive"
        })

        st.bar_chart(active_df.set_index("Status"))
        
elif menu == "👥 Customer Analytics":
    st.header("👥 Customer Analytics")
    
        # ================= Row 1 =================
    chart1, chart2 = st.columns(2)

    with chart1:
        st.subheader("📍 Customer Locations")

        customer_locations = db.fetch_data("""
            SELECT location,
                   COUNT(*) AS total_customers
            FROM customers
            GROUP BY location
            ORDER BY total_customers DESC
        """)

        customer_location_df = pd.DataFrame(
            customer_locations,
            columns=["Location", "Customers"]
        )

        st.bar_chart(customer_location_df.set_index("Location"))

    with chart2:
        st.subheader("⭐ Customer Rating Distribution")

        ratings = db.fetch_data("""
            SELECT average_rating,
                   COUNT(*) AS total_customers
            FROM customers
            GROUP BY average_rating
            ORDER BY average_rating
        """)

        rating_df = pd.DataFrame(
            ratings,
            columns=["Rating", "Customers"]
        )

        st.bar_chart(rating_df.set_index("Rating"))

    st.divider()

    # ================= Row 2 =================
    chart3, chart4 = st.columns(2)

    with chart3:
        st.subheader("👑 Top 10 Customers by Spending")

        customers = db.fetch_data("""
            SELECT
                c.name,
                SUM(o.total_amount) AS total_spent
            FROM customers c
            JOIN orders o
            ON c.customer_id = o.customer_id
            GROUP BY c.customer_id, c.name
            ORDER BY total_spent DESC
            LIMIT 10
        """)

        customer_df = pd.DataFrame(
            customers,
            columns=["Customer", "Total Spent"]
        )

        st.bar_chart(customer_df.set_index("Customer"))

    with chart4:
        st.subheader("🥘 Favorite Cuisine")

        cuisines = db.fetch_data("""
            SELECT preferred_cuisine,
                   COUNT(*) AS total_customers
            FROM customers
            GROUP BY preferred_cuisine
            ORDER BY total_customers DESC
        """)

        cuisine_df = pd.DataFrame(
            cuisines,
            columns=["Cuisine", "Customers"]
        )

        st.bar_chart(cuisine_df.set_index("Cuisine"))

    st.divider()
    
        # ================= Row 3 =================
    chart5, chart6 = st.columns(2)

    # ---------------- Chart 5 ----------------
    with chart5:
        st.subheader("💎 Premium vs Regular Customers")

        premium = db.fetch_data("""
            SELECT
                is_premium,
                COUNT(*) AS total_customers
            FROM customers
            GROUP BY is_premium
        """)

        premium_df = pd.DataFrame(
            premium,
            columns=["Type", "Customers"]
        )

        premium_df["Type"] = premium_df["Type"].replace({
            1: "Premium",
            0: "Regular"
        })

        st.bar_chart(premium_df.set_index("Type"))


    # ---------------- Chart 6 ----------------
    with chart6:
        st.subheader("📅 Customer Signups")

        signup = db.fetch_data("""
            SELECT
                signup_date,
                COUNT(*) AS total_customers
            FROM customers
            GROUP BY signup_date
            ORDER BY signup_date
        """)

        signup_df = pd.DataFrame(
            signup,
            columns=["Signup Date", "Customers"]
        )

        st.line_chart(signup_df.set_index("Signup Date"))

        
elif menu == "🛒 Order Analytics":
    st.header("🛒 Order Analytics")
    
        # ================= Row 1 =================
    chart1, chart2 = st.columns(2)

    with chart1:
        st.subheader("📈 Orders by Status")

        status = db.fetch_data("""
            SELECT status,
                   COUNT(*) AS total_orders
            FROM orders
            GROUP BY status
        """)

        status_df = pd.DataFrame(
            status,
            columns=["Status", "Orders"]
        )

        st.bar_chart(status_df.set_index("Status"))

    with chart2:
        st.subheader("💳 Payment Methods")

        payment = db.fetch_data("""
            SELECT payment_mode,
                   COUNT(*) AS total_orders
            FROM orders
            GROUP BY payment_mode
        """)

        payment_df = pd.DataFrame(
            payment,
            columns=["Payment Mode", "Orders"]
        )

        st.bar_chart(payment_df.set_index("Payment Mode"))

    st.divider()

    # ================= Row 2 =================
    chart3, chart4 = st.columns(2)

    with chart3:
        st.subheader("🍽 Top 10 Restaurants by Orders")

        restaurants = db.fetch_data("""
            SELECT
                r.name,
                COUNT(o.order_id) AS total_orders
            FROM restaurants r
            JOIN orders o
            ON r.restaurant_id = o.restaurant_id
            GROUP BY r.restaurant_id, r.name
            ORDER BY total_orders DESC
            LIMIT 10
        """)

        restaurant_df = pd.DataFrame(
            restaurants,
            columns=["Restaurant", "Orders"]
        )

        st.bar_chart(restaurant_df.set_index("Restaurant"))

    with chart4:
        st.subheader("👥 Top Customers by Orders")

        customers = db.fetch_data("""
            SELECT
                c.name,
                COUNT(o.order_id) AS total_orders
            FROM customers c
            JOIN orders o
            ON c.customer_id = o.customer_id
            GROUP BY c.customer_id, c.name
            ORDER BY total_orders DESC
            LIMIT 10
        """)

        customer_df = pd.DataFrame(
            customers,
            columns=["Customer", "Orders"]
        )

        st.bar_chart(customer_df.set_index("Customer"))

    st.divider()

    # ================= Row 3 =================
    chart5, chart6 = st.columns(2)

    with chart5:
        st.subheader("💰 Highest Order Amounts")

        amounts = db.fetch_data("""
            SELECT
                order_id,
                total_amount
            FROM orders
            ORDER BY total_amount DESC
            LIMIT 10
        """)

        amount_df = pd.DataFrame(
            amounts,
            columns=["Order ID", "Amount"]
        )

        st.bar_chart(amount_df.set_index("Order ID"))

    with chart6:
        st.subheader("⭐ Feedback Ratings")

        ratings = db.fetch_data("""
            SELECT
                feedback_rating,
                COUNT(*) AS total_orders
            FROM orders
            GROUP BY feedback_rating
            ORDER BY feedback_rating
        """)

        rating_df = pd.DataFrame(
            ratings,
            columns=["Rating", "Orders"]
        )

        st.bar_chart(rating_df.set_index("Rating"))
        
elif menu == "🛵 Delivery Person Analytics":
    st.header("🛵 Delivery Person Analytics")
        # ================= Row 1 =================
    chart1, chart2 = st.columns(2)

    with chart1:
        st.subheader("🏆 Top Delivery Persons by Deliveries")

        delivery_persons = db.fetch_data("""
            SELECT
                dp.name,
                COUNT(d.delivery_id) AS total_deliveries
            FROM delivery_persons dp
            JOIN deliveries d
            ON dp.delivery_person_id = d.delivery_person_id
            GROUP BY dp.delivery_person_id, dp.name
            ORDER BY total_deliveries DESC
            LIMIT 10
        """)

        delivery_df = pd.DataFrame(
            delivery_persons,
            columns=["Delivery Person", "Deliveries"]
        )

        st.bar_chart(delivery_df.set_index("Delivery Person"))

    with chart2:
        st.subheader("⭐ Delivery Person Ratings")

        ratings = db.fetch_data("""
            SELECT
            ROUND(Average_rating) as Rating,
                COUNT(*) AS total_persons
            FROM delivery_persons
            GROUP BY ROUND(average_rating)
            ORDER BY Rating
        """)

        rating_df = pd.DataFrame(
            ratings,
            columns=["Rating", "Delivery Persons"]
        )

        st.bar_chart(rating_df.set_index("Rating"))

    st.divider()

    # ================= Row 2 =================
    chart3, chart4 = st.columns(2)

    with chart3:
        st.subheader("🛵 Vehicle Types")

        vehicles = db.fetch_data("""
            SELECT
                vehicle_type,
                COUNT(*) AS total_persons
            FROM delivery_persons
            GROUP BY vehicle_type
            ORDER BY total_persons DESC
        """)

        vehicle_df = pd.DataFrame(
            vehicles,
            columns=["Vehicle", "Delivery Persons"]
        )

        st.bar_chart(vehicle_df.set_index("Vehicle"))

    with chart4:
        st.subheader("🏙️ Delivery Persons by City")

        cities = db.fetch_data("""
            SELECT
                location,
                COUNT(*) AS total_persons
            FROM delivery_persons
            GROUP BY location
            ORDER BY total_persons DESC
        """)

        city_df = pd.DataFrame(
            cities,
            columns=["location", "Delivery Persons"]
        )

        st.bar_chart(city_df.set_index("location"))

    st.divider()

    # ================= Row 3 =================
    chart5, chart6 = st.columns(2)

    with chart5:
        st.subheader("📦 Completed Deliveries")

        completed = db.fetch_data("""
            SELECT
                name,
                total_deliveries
            FROM delivery_persons
            ORDER BY total_deliveries DESC
            LIMIT 10
        """)

        completed_df = pd.DataFrame(
            completed,
            columns=["Delivery Person", "Completed Deliveries"]
        )

        st.bar_chart(completed_df.set_index("Delivery Person"))
        
            # ---------------- Chart 6 ----------------
    with chart6:
        st.subheader("⭐ Top Rated Delivery Persons")

        top_rated = db.fetch_data("""
            SELECT
                name,
                average_rating
            FROM delivery_persons
            ORDER BY average_rating DESC
            LIMIT 10
        """)

        top_rated_df = pd.DataFrame(
            top_rated,
            columns=["Delivery Person", "Average Rating"]
        )

        st.bar_chart(
            top_rated_df.set_index("Delivery Person")
        )

   
        
elif menu == "🚚 Delivery Analytics":
    st.header("🚚 Delivery Analytics")
    
        # ================= Row 1 =================
    chart1, chart2 = st.columns(2)

    with chart1:
        st.subheader("🚚 Delivery Status")

        delivery_status = db.fetch_data("""
            SELECT delivery_status,
                   COUNT(*) AS total_deliveries
            FROM deliveries
            GROUP BY delivery_status
        """)

        delivery_status_df = pd.DataFrame(
            delivery_status,
            columns=["Status", "Deliveries"]
        )

        st.bar_chart(delivery_status_df.set_index("Status"))

    with chart2:
        st.subheader("🛵 Vehicle Types")

        vehicles = db.fetch_data("""
            SELECT vehicle_type,
                   COUNT(*) AS total_deliveries
            FROM deliveries
            GROUP BY vehicle_type
            ORDER BY total_deliveries DESC
        """)

        vehicle_df = pd.DataFrame(
            vehicles,
            columns=["Vehicle", "Deliveries"]
        )

        st.bar_chart(vehicle_df.set_index("Vehicle"))

    st.divider()

    # ================= Row 2 =================
    chart3, chart4 = st.columns(2)

    with chart3:
        st.subheader("📏 Delivery Distance")

        distance = db.fetch_data("""
            SELECT
                delivery_id,
                distance
            FROM deliveries
            ORDER BY distance DESC
            LIMIT 10
        """)

        distance_df = pd.DataFrame(
            distance,
            columns=["Delivery ID", "Distance (km)"]
        )

        st.bar_chart(distance_df.set_index("Delivery ID"))

    with chart4:
        st.subheader("⏱ Delivery Time")

        delivery_time = db.fetch_data("""
            SELECT
                delivery_id,
                delivery_time
            FROM deliveries
            ORDER BY delivery_time DESC
            LIMIT 10
        """)

        delivery_time_df = pd.DataFrame(
            delivery_time,
            columns=["Delivery ID", "Time (min)"]
        )

        st.bar_chart(delivery_time_df.set_index("Delivery ID"))

    st.divider()

    # ================= Row 3 =================
    chart5, chart6 = st.columns(2)

    with chart5:
        st.subheader("💰 Highest Delivery Fees")

        fees = db.fetch_data("""
            SELECT
                delivery_id,
                delivery_fee
            FROM deliveries
            ORDER BY delivery_fee DESC
            LIMIT 10
        """)

        fee_df = pd.DataFrame(
            fees,
            columns=["Delivery ID", "Fee"]
        )

        st.bar_chart(fee_df.set_index("Delivery ID"))

    with chart6:
        st.subheader("⌛ Estimated Delivery Time")

        estimated = db.fetch_data("""
            SELECT
                delivery_id,
                estimated_time
            FROM deliveries
            ORDER BY estimated_time DESC
            LIMIT 10
        """)

        estimated_df = pd.DataFrame(
            estimated,
            columns=["Delivery ID", "Estimated Time (min)"]
        )

        st.bar_chart(estimated_df.set_index("Delivery ID"))
        
        
        
        
    
        
        
        
        
    
    
        
        
    
        
        
   
            

            

            
            
            
            
            
            
        
            


            
            
            
            
            
            
    
            
            
                
            
            
                    
                            
            
            
            

            

        
            
            
            
            
            
            
            
            
            
    
        

    
    
    
    
    

# Customers
elif menu == "Customers":
    customers = db.fetch_data("SELECT * FROM customers LIMIT 5")

    df = pd.DataFrame(
        customers,
        columns=[
            "ID",
            "Name",
            "Email",
            "Phone",
            "Address",
            "Join Date",
            "Premium",
            "Favorite Cuisine",
            "Rating",
            "Total Orders"
        ]
    )

    st.subheader("Customers")
    st.dataframe(df)

# Orders
elif menu == "Orders":
    orders = db.fetch_data("SELECT * FROM orders LIMIT 5")
    

    df = pd.DataFrame(
        orders,
        columns=[
            "Order ID",
            "Customer ID",
            "Restaurant ID",
            "Order Date",
            "Delivery Time",
            "Status",
            "Amount",
            "Payment Method",
            "Delivery Fee",
            "Delivery Person ID"
            
        ]
    )

    st.subheader("Orders")
    st.dataframe(df)
    
    # Delivery Persons
    # Delivery Persons
elif menu == "Delivery Persons":

    delivery_persons = db.fetch_data("SELECT * FROM delivery_persons LIMIT 5")
    

    df = pd.DataFrame(
        delivery_persons,
        columns=[
            "ID",
            "Name",
            "Phone",
            "Vehicle",
            "Completed Deliveries",
            "Rating",
            "City"
        ]
    )

    st.subheader("Delivery Persons")
    st.dataframe(df)
    
elif menu == "Deliveries":

    deliveries = db.fetch_data("SELECT * FROM deliveries LIMIT 5")

    df = pd.DataFrame(
        deliveries,
        columns=[
            "Delivery ID",
            "Order ID",
            "Delivery Person ID",
            "Status",
            "Distance (km)",
            "Delivery Time (min)",
            "Customer Rating",
            "Delivery Cost",
            "Vehicle"
        ]
    )

    st.subheader("Deliveries")
    st.dataframe(df)
    
    
elif menu == "Add Restaurants":

    st.header("🍽️ Add Restaurant")

    restaurant_id = st.number_input(
        "Restaurant ID",
        min_value=1,
        step=1
    )

    name = st.text_input("Restaurant Name")

    cuisine_type = st.text_input("Cuisine Type")

    location = st.text_input("Location")

    owner_name = st.text_input("Owner Name")

    average_delivery_time = st.number_input(
        "Average Delivery Time (Minutes)",
        min_value=1,
        step=1
    )

    contact_number = st.text_input("Contact Number")

    rating = st.number_input(
        "Rating",
        min_value=0.0,
        max_value=5.0,
        step=0.1
    )

    total_orders = st.number_input(
        "Total Orders",
        min_value=0,
        step=1
    )

    is_active = st.selectbox(
        "Restaurant Status",
        [1, 0],
        format_func=lambda x: "Active" if x == 1 else "Inactive"
    )

    if st.button("Add Restaurant"):

        query = f"""
        INSERT INTO restaurants
        (
            restaurant_id,
            name,
            cuisine_type,
            location,
            owner_name,
            average_delivery_time,
            contact_number,
            rating,
            total_orders,
            is_active
        )
        VALUES
        (
            {restaurant_id},
            '{name}',
            '{cuisine_type}',
            '{location}',
            '{owner_name}',
            {average_delivery_time},
            '{contact_number}',
            {rating},
            {total_orders},
            {is_active}
        )
        """

        db.execute_query(query)

        st.success("✅ Restaurant Added Successfully!")
    
elif menu == "Adding New Customer":
    st.header("➕ Add New Customer")
    customer_id = st.number_input("Customer ID", step=1)
    name = st.text_input("Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone")
    location = st.text_input("Address")
    join_date = st.date_input("Join Date")
    premium = st.selectbox(
        "Premium",
        [1,0],
        format_func=lambda x: "Yes" if x == 1
        else "No"
    )
    
    favourite = st.text_input("Favourite Cuisine")
    rating = st.number_input("Rating", 0.0, 5.0)
    total_orders = st.number_input("Total Orders", step=1)

    if st.button("Add Customer"):

        query = f"""
        INSERT INTO customers
        VALUES (
        {customer_id},
        '{name}',
        '{email}',
        '{phone}',
        '{location}',
        '{join_date}',
        '{premium}',
        '{favourite}',
        {rating},
        {total_orders}
        )
        """
        db.execute_query(query)
        st.success("Customer Added Successfully!")
        
elif menu == "Restaurants":
    restaurants = db.fetch_data("SELECT * FROM restaurants LIMIT 5")

    df = pd.DataFrame(
        restaurants,
        columns=[
            "ID",
            "Restaurant",
            "Cuisine",
            "City",
            "Owner",
            "Tables",
            "Phone",
            "Rating",
            "Orders",
            "Active"
        ]
    )

    st.subheader("Restaurants")
    st.dataframe(df)

    st.subheader("🔍 Search Customer")

    search_name = st.text_input("Search Customer")

    if st.button("Search"):
        query = f"""
        SELECT * FROM customers
        WHERE name LIKE '%{search_name}%'
        """

        result = db.fetch_data(query)

        if result:
            st.dataframe(result)
        else:
            st.warning("Customer not found.")
        
        

        
        query = f"""
        INSERT INTO restaurants
        (restaurant_id , name , location , cuisine_type , owner_name , rating , average_delivery_time , contact_number , total_orders , is_active)
        
        VALUES
        ('{restaurant_id}','{name}','{location}','{cuisine}','{owner_name}','{rating}','{delivery_time}','{contact}',0,1) """
    

        db.execute_query(query)

        st.success("Restaurant Added Successfully!")
            

        
elif menu == "Add Order":

    st.subheader("🛒 Add Order")

    order_id = st.number_input(
        "Order ID",
        min_value=1,
        step=1
    )
    
    customer_result = db.fetch_data("SELECT customer_id FROM customers")
    customer_ids = [row[0] for row in customer_result]
    

    restaurant_result = db.fetch_data("SELECT restaurant_id FROM restaurants")
    restaurant_ids = [row[0] for row in restaurant_result]
    # Check if data exists
    if not customer_ids:
        st.error("No customers found. Please add a customer first.")
        st.stop()
        
        
        if not restaurant_ids:
            
            st.error("No restaurants found. Please add a restaurant first.")
            st.stop()
            
            order_id = st.number_input("Order ID", min_value=1, step=1)
    
    
    
    
    
    
    customer_id = st.selectbox("Customer", customer_ids)
    restaurant_id = st.selectbox("Restaurant", restaurant_ids)




    order_amount = st.number_input(
        "Total Amount",
        min_value=0.0
    )
    

    
    order_date = st.date_input("Order Date")
    delivery_date = st.date_input("Delivery Date")
    delivery_clock = st.time_input("Delivery Time")
    
    
    from datetime import datetime
    delivery_time = datetime.combine(delivery_date, delivery_clock)
    
    

    

    status = st.selectbox(
        "Status",
        ["Pending", "Preparing", "Delivered", "Cancelled"]
    )

    payment_mode = st.selectbox(
        "Payment Mode",
        ["Cash", "UPI", "Card"]
    )

    discount_applied = st.number_input(
        "Discount Applied",
        min_value=0.0
    )

    feedback_rating = st.number_input(
        "Feedback Rating",
        min_value=0.0,
        max_value=5.0,
        step=0.5
    )

    if st.button("Add Order"):

        query = f"""
        INSERT INTO orders
        (
            order_id,
            customer_id,
            restaurant_id,
            order_date,
            delivery_time,
            status,
            total_amount,
            payment_mode,
            discount_applied,
            feedback_rating
        )

        VALUES
        (
            {order_id},
            {customer_id},
            {restaurant_id},
            '{order_date}',
            '{delivery_time.strftime("%Y-%m-%d %H:%M:%S")}',
            '{status}',
            {order_amount},
            '{payment_mode}',
            {discount_applied},
            {feedback_rating}
        )
        """
        
        st.code(query)
        db.execute_query(query)

        st.success("✅ Order Added Successfully!")

        
elif menu == "Add Delivery Person":

    st.subheader("🛵 Add Delivery Person")

    person_id = st.number_input("Delivery Person ID", min_value=1, step=1)
    name = st.text_input("Name")
    phone = st.text_input("Phone Number")
    vehicle = st.text_input("Vehicle")
    completed = st.number_input("Completed Deliveries", min_value=0, step=1)
    rating = st.number_input("Rating", 0.0, 5.0, 0.0)
    city = st.text_input("City")
    
    
    if st.button("Add Delivery Person"):
        

        query = f"""
        INSERT INTO delivery_persons
        VALUES (
        {person_id},
        '{name}',
        '{phone}',
        '{vehicle}',
        {completed},
        {rating},
        '{city}'
        )
        """

    db.execute_query(query)

    st.success("Delivery Person Added Successfully!")
    
elif menu == "Add Delivery":

    st.subheader("🚚 Add Delivery")

    delivery_id = st.number_input("Delivery ID", min_value=1, step=1)

    order_id = st.number_input("Order ID", min_value=1, step=1)

    delivery_person_id = st.number_input("Delivery Person ID", min_value=1, step=1)
    
    
    status_options = [
        
        "Pending",
        "On the way",
        "Delivered",
        "Cancelled"
        ]
    
    

    delivery_status = st.selectbox(
        "Delivery Status",
        status_options
        )



    distance = st.number_input(
        "Distance (km)",
        min_value=0.0
    )

    delivery_time = st.number_input(
        "Delivery Time (minutes)",
        min_value=0
    )

    estimated_time = st.number_input(
        "Estimated Time (minutes)",
        min_value=0
    )

    delivery_fee = st.number_input(
        "Delivery Fee",
        min_value=0.0
    )

    vehicle_type = st.selectbox(
        "Vehicle Type",
        ["Bike", "Scooter", "Cycle", "Car"]
    )

    if st.button("Add Delivery"):

        query = f"""
        INSERT INTO deliveries
        VALUES(
            {delivery_id},
            {order_id},
            {delivery_person_id},
            '{delivery_status}',
            {distance},
            {delivery_time},
            {estimated_time},
            {delivery_fee},
            '{vehicle_type}'
        )
        """

        db.execute_query(query)

        st.success("Delivery Added Successfully!")
        
elif menu == "Update Customer":

    st.subheader("✏️ Update Customer")

    customer_id = st.number_input("Customer ID", min_value=1, step=1)

    if "customer_data" not in st.session_state:
        st.session_state.customer_data = None

    if st.button("Load Customer"):

        query = f"SELECT * FROM customers WHERE customer_id={customer_id}"
        result = db.fetch_data(query)

        if result:
            st.session_state.customer_data = result[0]
        else:
            st.error("Customer not found.")

    if st.session_state.customer_data:

        customer = st.session_state.customer_data

        name = st.text_input("Name", value=customer[1])
        email = st.text_input("Email", value=customer[2])
        phone = st.text_input("Phone", value=customer[3])
        location = st.text_input("address", value=customer[4])

        if st.button("Update Customer"):

            update_query = f"""
            UPDATE customers
            SET
                name='{name}',
                email='{email}',
                phone='{phone}',
                location='{location}'
            WHERE customer_id={customer_id}
            """

            db.execute_query(update_query)

            st.success("✅ Customer Updated Successfully!")

            st.session_state.customer_data = None
            
elif menu == "Update Restaurant":

    st.subheader("🍽️ Update Restaurant")

    restaurant_id = st.number_input("Restaurant ID", min_value=1, step=1)

    if "restaurant_data" not in st.session_state:
        st.session_state.restaurant_data = None

    if st.button("Load Restaurant"):

        query = f"SELECT * FROM restaurants WHERE restaurant_id={restaurant_id}"
        result = db.fetch_data(query)

        if result:
            st.session_state.restaurant_data = result[0]
        else:
            st.error("Restaurant not found.")

    if st.session_state.restaurant_data:

        restaurant = st.session_state.restaurant_data

        name = st.text_input("Restaurant Name", value=restaurant[1])
        cuisine_type = st.text_input("Cuisine Type", value=restaurant[2])
        location = st.text_input("Location", value=restaurant[3])
        owner_name = st.text_input("Owner Name", value=restaurant[4])

        average_delivery_time = st.number_input(
            "Average Delivery Time",
            min_value=1,
            value=int(restaurant[5])
        )

        contact_number = st.text_input(
            "Contact Number",
            value=restaurant[6]
        )

        rating = st.number_input(
            "Rating",
            min_value=0.0,
            max_value=5.0,
            value=float(restaurant[7])
        )

        total_orders = st.number_input(
            "Total Orders",
            min_value=0,
            value=int(restaurant[8])
        )

        is_active = st.selectbox(
            "Is Active",
            [0, 1],
            index=int(restaurant[9])
        )

        if st.button("Update Restaurant"):

            update_query = f"""
            UPDATE restaurants
            SET
                name='{name}',
                cuisine_type='{cuisine_type}',
                location='{location}',
                owner_name='{owner_name}',
                average_delivery_time={average_delivery_time},
                contact_number='{contact_number}',
                rating={rating},
                total_orders={total_orders},
                is_active={is_active}
            WHERE restaurant_id={restaurant_id}
            """

            db.execute_query(update_query)

            st.success("✅ Restaurant Updated Successfully!")

            st.session_state.restaurant_data = None

elif menu == "Delete Customer":

    st.subheader("🗑️ Delete Customer")

    customer_id = st.number_input(
        "Customer ID",
        min_value=1,
        step=1
    )

    if st.button("Delete Customer"):

        # Check whether customer exists
        query = f"SELECT * FROM customers WHERE customer_id={customer_id}"
        result = db.fetch_data(query)

        if result:

            # Get all order IDs of this customer
            orders = db.fetch_data(
                f"SELECT order_id FROM orders WHERE customer_id={customer_id}"
            )

            st.write("Orders:", orders)

            # Delete deliveries for each order
            for row in orders:

                order_id = row[0]

                st.write(f"Deleting deliveries for Order ID: {order_id}")

                db.execute_query(
                    f"DELETE FROM deliveries WHERE order_id={order_id}"
                )

            st.success("✅ All related deliveries deleted.")

            # Delete all orders of the customer
            db.execute_query(
                f"DELETE FROM orders WHERE customer_id={customer_id}"
            )

            st.success("✅ All related orders deleted.")

            # Delete the customer
            db.execute_query(
                f"DELETE FROM customers WHERE customer_id={customer_id}"
            )

            st.success("✅ Customer Deleted Successfully!")

        else:
            st.error("❌ Customer ID not found.")
            
elif menu == "Delete Restaurant":

    st.subheader("🗑️ Delete Restaurant")

    restaurant_id = st.number_input(
        "Restaurant ID",
        min_value=1,
        step=1
    )

    if st.button("Delete Restaurant"):

        # Check whether restaurant exists
        query = f"SELECT * FROM restaurants WHERE restaurant_id={restaurant_id}"
        result = db.fetch_data(query)

        if result:

            # Get all orders of this restaurant
            orders = db.fetch_data(
                f"SELECT order_id FROM orders WHERE restaurant_id={restaurant_id}"
            )

            st.write("Orders:", orders)

            # Delete deliveries for each order
            for row in orders:

                order_id = row[0]

                st.write(f"Deleting deliveries for Order ID: {order_id}")

                db.execute_query(
                    f"DELETE FROM deliveries WHERE order_id={order_id}"
                )

            st.success("✅ All related deliveries deleted.")

            # Delete all orders of the restaurant
            db.execute_query(
                f"DELETE FROM orders WHERE restaurant_id={restaurant_id}"
            )

            st.success("✅ All related orders deleted.")

            # Delete the restaurant
            db.execute_query(
                f"DELETE FROM restaurants WHERE restaurant_id={restaurant_id}"
            )

            st.success("✅ Restaurant Deleted Successfully!")

        else:
            st.error("❌ Restaurant ID not found.")
elif menu == "Search Order":

    st.subheader("🔍 Search Order")

    order_id = st.number_input(
        "Enter Order ID",
        min_value=1,
        step=1
    )

    if st.button("Search Order"):

        query = f"SELECT * FROM orders WHERE order_id={order_id}"

        result = db.fetch_data(query)

        if result:

            order = result[0]

            st.success("✅ Order Found")

            st.write("### Order Details")

            st.write("Order ID:", order[0])
            st.write("Customer ID:", order[1])
            st.write("Restaurant ID:", order[2])
            st.write("Order Date:", order[3])
            st.write("Delivery Time:", order[4])
            st.write("Status:", order[5])
            st.write("Total Amount:", order[6])
            st.write("Payment Mode:", order[7])
            st.write("Discount Applied:", order[8])
            st.write("Feedback Rating:", order[9])

        else:
            st.error("❌ Order not found.")
            
elif menu == "Search Delivery":

    st.subheader("🚚 Search Delivery")

    delivery_id = st.number_input(
        "Enter Delivery ID",
        min_value=1,
        step=1
    )

    if st.button("Search Delivery"):

        query = f"""
        SELECT *
        FROM deliveries
        WHERE delivery_id={delivery_id}
        """

        result = db.fetch_data(query)

        if result:

            delivery = result[0]

            st.success("✅ Delivery Found")

            st.write("### Delivery Details")

            st.write("Delivery ID:", delivery[0])
            st.write("Order ID:", delivery[1])
            st.write("Delivery Person ID:", delivery[2])
            st.write("Delivery Status:", delivery[3])
            st.write("Distance (km):", delivery[4])
            st.write("Delivery Time (minutes):", delivery[5])
            st.write("Estimated Time (minutes):", delivery[6])
            st.write("Delivery Fee:", delivery[7])
            st.write("Vehicle Type:", delivery[8])

        else:
            st.error("❌ Delivery not found.")
elif menu == "Update Order":

    st.subheader("✏️ Update Order")

    order_id = st.number_input(
        "Order ID",
        min_value=1,
        step=1
    )

    if "order_data" not in st.session_state:
        st.session_state.order_data = None

    if st.button("Load Order"):

        query = f"SELECT * FROM orders WHERE order_id={order_id}"
        result = db.fetch_data(query)

        if result:
            st.session_state.order_data = result[0]
        else:
            st.error("❌ Order not found.")

    if st.session_state.order_data:

        order = st.session_state.order_data

        customer_id = st.number_input(
            "Customer ID",
            min_value=1,
            value=int(order[1])
        )

        restaurant_id = st.number_input(
            "Restaurant ID",
            min_value=1,
            value=int(order[2])
        )

        order_date = st.text_input(
            "Order Date (YYYY-MM-DD HH:MM:SS)",
            value=str(order[3])
        )

        delivery_time = st.text_input(
            "Delivery Time (YYYY-MM-DD HH:MM:SS)",
            value=str(order[4])
        )

        status = st.selectbox(
            "Status",
            ["Pending", "Delivered", "Cancelled"],
            index=["Pending", "Delivered", "Cancelled"].index(order[5])
        )

        total_amount = st.number_input(
            "Total Amount",
            min_value=0.0,
            value=float(order[6]),
            step=1.0
        )

        payment_mode = st.text_input(
            "Payment Mode",
            value=order[7]
        )

        discount_applied = st.number_input(
            "Discount Applied",
            min_value=0.0,
            value=float(order[8]),
            step=1.0
        )

        feedback_rating = st.number_input(
            "Feedback Rating",
            min_value=0,
            max_value=5,
            value=int(order[9])
        )

        if st.button("Update Order"):

            update_query = f"""
            UPDATE orders
            SET
                customer_id={customer_id},
                restaurant_id={restaurant_id},
                order_date='{order_date}',
                delivery_time='{delivery_time}',
                status='{status}',
                total_amount={total_amount},
                payment_mode='{payment_mode}',
                discount_applied={discount_applied},
                feedback_rating={feedback_rating}
            WHERE order_id={order_id}
            """

            db.execute_query(update_query)

            st.success("✅ Order Updated Successfully!")

            st.session_state.order_data = None
            
elif menu == "Delete Order":

    st.subheader("🗑️ Delete Order")

    order_id = st.number_input(
        "Order ID",
        min_value=1,
        step=1
    )

    if st.button("Delete Order"):

        # Check whether the order exists
        query = f"SELECT * FROM orders WHERE order_id={order_id}"
        result = db.fetch_data(query)

        if result:

            # Delete delivery related to this order
            db.execute_query(
                f"DELETE FROM deliveries WHERE order_id={order_id}"
            )

            st.success("✅ Related delivery deleted.")

            # Delete the order
            db.execute_query(
                f"DELETE FROM orders WHERE order_id={order_id}"
            )

            st.success("✅ Order Deleted Successfully!")

        else:
            st.error("❌ Order ID not found.")

elif menu == "Update Delivery":

    st.subheader("✏️ Update Delivery")

    delivery_id = st.number_input(
        "Delivery ID",
        min_value=1,
        step=1
    )

    if "delivery_data" not in st.session_state:
        st.session_state.delivery_data = None

    if st.button("Load Delivery"):

        query = f"SELECT * FROM deliveries WHERE delivery_id={delivery_id}"
        result = db.fetch_data(query)

        if result:
            st.session_state.delivery_data = result[0]
        else:
            st.error("❌ Delivery not found.")

    if st.session_state.delivery_data:

        delivery = st.session_state.delivery_data

        order_id = st.number_input(
            "Order ID",
            min_value=1,
            value=int(delivery[1])
        )

        delivery_person_id = st.number_input(
            "Delivery Person ID",
            min_value=1,
            value=int(delivery[2])
        )
        
        status_options = [
            
            "Pending",
            "On the way",
            "Delivered",
            "Cancelled"
            ]
        delivery_status = st.selectbox(
            "Delivery Status",
            status_options,
            index=status_options.index(delivery[3])
            )
        
    

    

        distance = st.number_input(
            "Distance (km)",
            min_value=0.0,
            value=float(delivery[4])
        )

        delivery_time = st.number_input(
            "Delivery Time (minutes)",
            min_value=0,
            value=int(delivery[5])
        )

        estimated_time = st.number_input(
            "Estimated Time (minutes)",
            min_value=0,
            value=int(delivery[6])
        )

        delivery_fee = st.number_input(
            "Delivery Fee",
            min_value=0.0,
            value=float(delivery[7])
        )

        vehicle_type = st.text_input(
            "Vehicle Type",
            value=delivery[8]
        )

        if st.button("Update Delivery"):

            update_query = f"""
            UPDATE deliveries
            SET
                order_id={order_id},
                delivery_person_id={delivery_person_id},
                delivery_status='{delivery_status}',
                distance={distance},
                delivery_time={delivery_time},
                estimated_time={estimated_time},
                delivery_fee={delivery_fee},
                vehicle_type='{vehicle_type}'
            WHERE delivery_id={delivery_id}
            """

            db.execute_query(update_query)

            st.success("✅ Delivery Updated Successfully!")

            st.session_state.delivery_data = None
            
elif menu == "Delete Delivery":

    st.subheader("🗑️ Delete Delivery")

    delivery_id = st.number_input(
        "Delivery ID",
        min_value=1,
        step=1
    )

    if st.button("Delete Delivery"):

        # Check if delivery exists
        query = f"SELECT * FROM deliveries WHERE delivery_id={delivery_id}"
        result = db.fetch_data(query)

        if result:

            db.execute_query(
                f"DELETE FROM deliveries WHERE delivery_id={delivery_id}"
            )

            st.success("✅ Delivery Deleted Successfully!")

        else:
            st.error("❌ Delivery ID not found.")                                    
                
                
                
                
            

                
            
            

                
                
                

            
                
                
                

            

        
        
        
        



    

            
            
            
            
            
