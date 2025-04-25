import Footer from "../components/common/Footer";
import CTAButton from "../components/core/HomePage/Button";
import HighlightText from "../components/core/HomePage/HighlightText";
import NewsImage1 from "../assets/Images/fake-news-1.png";
import NewsImage2 from "../assets/Images/fake-news-2.png";
import NewsImage3 from "../assets/Images/fake-news-3.jpeg";
import NewsImage4 from "../assets/Images/fake-news-4.png";

const Home = () => {
  return (
    <div>
      {/* Section 1 - Hero Section */}
      <div className="relative mx-auto flex flex-col w-11/12 max-w-maxContent items-center text-white justify-between md:gap-8">
        {/* Section 1 - Introduction */}
        <div className="flex flex-col md:flex-row justify-between items-center my-16">
          {/* Left Part */}
          <div className="w-[100%] md:w-[50%]">
            <div className="text-3xl sm:text-4xl font-semibold mb-7">
              Unmasking Lies with
              <HighlightText text={" AI-Powered Fake News Detection"} />
            </div>

            <div className="text-md sm:text-lg font-bold text-richblack-200">
              Detect misinformation with cutting-edge Machine Learning and NLP
              algorithms. Verify news authenticity instantly with our hybrid
              BGWO-PSO model.
            </div>

            <div className="flex mt-8">
              <CTAButton active={true} linkto={"/predict"}>
                Try Now
              </CTAButton>
            </div>
          </div>

          {/* Right Part */}

          <div className="w-[100%] md:w-[50%] flex justify-center items-center mt-16 md:mt-0">
            <img src={NewsImage1} width={"80%"} alt="Fake News Detection" />
          </div>
        </div>

        {/* Section 2 - Feature 1 */}
        <div className="flex flex-col-reverse md:flex-row justify-center items-center gap-10 sm:gap-20 mb-10">
          <div className="w-[100%] md:w-[50%] flex justify-center items-center">
            <img
              src={NewsImage2}
              alt="News Scraping"
              className="w-[60%] md:w-[90%]"
            />
          </div>

          {/* left part */}
          <div className="w-[100%] md:w-[50%] flex flex-col gap-6">
            <div className="text-3xl sm:text-4xl font-semibold mt-10">
              Scrape and Analyze News from
              <HighlightText text={" Any Website"} />
            </div>

            <div className="w-[90%] text-lg md:text-xl font-bold text-richblack-200">
              Automatically extract news content using BeautifulSoup and analyze
              its authenticity using our hybrid machine learning model.
            </div>

            <div className="flex flex-row gap-7 mt-8">
              <CTAButton active={true} linkto={"/predict"}>
                Try URL Input
              </CTAButton>
            </div>
          </div>
        </div>

        {/* Section 3 - Feature 2 */}
        <div className="flex flex-col md:flex-row justify-center items-center mt-10 gap-10 sm:gap-20 mb-10">
          {/* left part */}
          <div className="w-[100%] md:w-[50%] flex flex-col gap-6">
            <div className="text-3xl sm:text-4xl font-semibold mt-10">
              Advanced Nature Inspired Computing Algorithm
              <HighlightText text={" BGWOPSO"} />
            </div>

            <div className="w-[90%] text-lg sm:text-xl font-bold text-richblack-200">
              Our model optimizes features using Hybrid Big Grey Wolf Optimization and Particle Swarm Optimization (BGWOPSO) Algorithms
            </div>

            <div className="flex flex-row gap-7 mt-8">
              <CTAButton active={true} linkto={"/predict"}>
                Check News
              </CTAButton>
            </div>
          </div>

          <div className="w-[100%] md:w-[50%] flex justify-center items-center">
            <img
              src={NewsImage3}
              alt="SMOTE Balancing"
              className="w-[60%] md:w-[90%]"
            />
          </div>
        </div>

        {/* Section 4 - Truth Icon with DB System */}
        <div className="flex flex-col-reverse md:flex-row justify-center mt-16 mb-24 items-center gap-10 md:gap-10">
          {/* left part */}
          <div className="w-[100%] md:w-[50%] flex justify-center items-center">
            <img
              src={NewsImage4}
              alt="games"
              loading="lazy"
              className="w-[70%] md:w-[90%]"
            />
          </div>

          {/* Right Side */}
          <div className="w-[100%] md:w-[50%] flex flex-col gap-6">
            <div className="text-3xl sm:text-4xl font-semibold mt-10">
              Continuous Retraining with
              <HighlightText text={" User Feedback"} />
            </div>

            <div className="w-[90%] text-md sm:text-lg font-bold text-richblack-200">
              Every user input is automatically stored in our MongoDB database
              for future model retraining — keeping our detection system always
              updated.
            </div>

            <div className="flex flex-row gap-7 mt-8">
              <CTAButton active={true} linkto={"/about"}>
                Learn More
              </CTAButton>
            </div>
          </div>
        </div>
      </div>

      {/* Footer */}
      <Footer />
    </div>
  );
};

export default Home;
