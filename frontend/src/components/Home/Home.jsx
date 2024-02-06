// import React, { useState, useEffect } from 'react';
// import './Home.css';

// const Home = () => {
//   const [showWelcomeMessage, setShowWelcomeMessage] = useState(false);
//   const [featuredPromotions, setFeaturedPromotions] = useState([]);
//   const [businesses, setBusinesses] = useState([]);

//   useEffect(() => {
//     const intervalId = setInterval(() => {
//       setShowWelcomeMessage((prev) => !prev);
//     }, 3000);

//     // Cleanup the interval on component unmount
//     return () => clearInterval(intervalId);
//   }, []); // Empty dependency array ensures the effect runs only once on mount

//   const handleLoginClick = () => {
//     // Perform login logic
//     // For demonstration purposes, let's hide the welcome message on login click
//     setShowWelcomeMessage(false);
//   };

//   return (
//     <div className="home-container">
//       <div className={`welcome-message ${showWelcomeMessage ? 'visible' : ''}`}>
//         Register to promote your business and view upcoming offers and discounts
//       </div>
//       <div className="promo-section">
//         <div className="login-button" onClick={handleLoginClick}>
//           PROMOTE YOUR BIZ
//         </div>
//       </div>
//       <div className="search-section">
//         <div className="search-text">Discover businesses around you</div>
//         <input type="text" placeholder="Search for a business" className="search-box" />
//       </div>
//       {/* Add your carousel component here */}
//     </div>
//   );
// };

// export default Home;





// import React, { useState, useEffect } from 'react';
// import Slider from 'react-slick';
// import './Home.css';

// const Home = () => {
//   const [showWelcomeMessage, setShowWelcomeMessage] = useState(false);
//   const [featuredPromotions, setFeaturedPromotions] = useState([]);
//   const [businesses, setBusinesses] = useState([]);

//   useEffect(() => {
//     // Fetch featured promotions
//     fetch('/promotion')
//       .then(response => response.json())
//       .then(data => setFeaturedPromotions(data))
//       .catch(error => console.error('Error fetching featured promotions:', error));

//     // Fetch businesses
//     fetch('/business')
//       .then(response => response.json())
//       .then(data => setBusinesses(data))
//       .catch(error => console.error('Error fetching businesses:', error));

//     // Interval for showing/hiding welcome message
//     const intervalId = setInterval(() => {
//       setShowWelcomeMessage(prev => !prev);
//     }, 3000);

//     // Cleanup the interval on component unmount
//     return () => clearInterval(intervalId);
//   }, []); // Empty dependency array ensures the effect runs only once on mount

//   const handleLoginClick = () => {
//     // Perform login logic
//     // For demonstration purposes, let's hide the welcome message on login click
//     setShowWelcomeMessage(false);
//   };

//   // Slick slider settings
//   const sliderSettings = {
//     dots: true,
//     infinite: true,
//     speed: 500,
//     slidesToShow: 1,
//     slidesToScroll: 1,
//   };

//   return (
//     <div className="home-container">
//       <div className={`welcome-message ${showWelcomeMessage ? 'visible' : ''}`}>
//         Register to promote your business and view upcoming offers and discounts
//       </div>

//       {/* Featured Promotions Slider */}
//       <div className="promo-section">
//         <h2 className="promo-text">Featured Promotions</h2>
//         <Slider {...sliderSettings}>
//           {featuredPromotions.map(promotion => (
//             <div key={promotion.id} className="featured-promotion">
//               <h3>{promotion.title}</h3>
//               <p>{promotion.description}</p>
//             </div>
//           ))}
//         </Slider>
//       </div>

//       {/* Businesses Section */}
//       <div className="business-section">
//         <h2 className="business-text">Explore Local Businesses</h2>
//         <div className="business-list">
//           {businesses.map(business => (
//             <div key={business.id} className="business-card">
//               <h3>{business.name}</h3>
//               <p>{business.description}</p>
//             </div>
//           ))}
//         </div>
//       </div>

//       <div className="search-section">
//         <div className="search-text">Discover businesses around you</div>
//         <input type="text" placeholder="Search for a business" className="search-box" />
//       </div>
//     </div>
//   );
// };

// export default Home;




import React, { useState, useEffect } from 'react';
import Slider from 'react-slick';
import './Home.css';

const Home = () => {
  const [showWelcomeMessage, setShowWelcomeMessage] = useState(false);
  const [featuredPromotions, setFeaturedPromotions] = useState([]);
  const [businesses, setBusinesses] = useState([]);

  useEffect(() => {
    // Fetch featured promotions
    fetch('/promotion')
      .then(response => response.json())
      .then(data => setFeaturedPromotions(data))
      .catch(error => console.error('Error fetching featured promotions:', error));

    // Fetch businesses
    fetch('/business')
      .then(response => response.json())
      .then(data => setBusinesses(data))
      .catch(error => console.error('Error fetching businesses:', error));

    // Interval for showing/hiding welcome message
    const intervalId = setInterval(() => {
      setShowWelcomeMessage(prev => !prev);
    }, 3000);

    // Cleanup the interval on component unmount
    return () => clearInterval(intervalId);
  }, []); // Empty dependency array ensures the effect runs only once on mount

  const handleLoginClick = () => {
    // Perform login logic
    // For demonstration purposes, let's hide the welcome message on login click
    setShowWelcomeMessage(false);
  };

  // Slick slider settings for Featured Promotions
  const featuredPromotionsSliderSettings = {
    dots: true,
    infinite: true,
    speed: 500,
    slidesToShow: 1,
    slidesToScroll: 1,
  };

  return (
    <div className="home-container">
      <div className={`welcome-message ${showWelcomeMessage ? 'visible' : ''}`}>
        Register to promote your business and view upcoming offers and discounts
      </div>

      {/* Featured Promotions Slider */}
      <div className="promo-section">
         <div className="login-button" onClick={handleLoginClick}>
           PROMOTE YOUR BIZ
         </div>

        <h2 className="promo-text">Featured Promotions</h2>
        <Slider {...featuredPromotionsSliderSettings}>
          {featuredPromotions.map(promotion => (
            <div key={promotion.id} className="featured-promotion">
              <h3>{promotion.title}</h3>
              <p>{promotion.description}</p>
            </div>
          ))}
        </Slider>
      </div>

      {/* Businesses Section */}
      <div className="business-section">
        <h2 className="business-text">Explore Local Businesses</h2>
        <div className="business-list">
          {businesses.map(business => (
            <div key={business.id} className="business-card">
              <h3>{business.name}</h3>
              <p>{business.description}</p>
            </div>
          ))}
        </div>
      </div>

      <div className="search-section">
        <div className="search-text">Discover businesses around you</div>
        <input type="text" placeholder="Search for a business" className="search-box" />
      </div>
    </div>
  );
};

export default Home;
