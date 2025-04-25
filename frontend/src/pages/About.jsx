import AboutUs from "../assets/Images/founding_story.png";

import ContactFormSection from "../components/core/AboutPage/ContactFormSection";
import HighlightText from "../components/core/HomePage/HighlightText";
import Footer from "../components/common/Footer";

const About = () => {
  return (
    <div>
      <section>
        <div className="mx-auto flex w-11/12 max-w-maxContent flex-col justify-between gap-10 text-richblack-500">
          <div className="relative mx-auto flex w-11/12 max-w-maxContent flex-col justify-between gap-10 text-start lg:text-center text-white">
            <header className="mx-auto pt-16 pb-10 text-3xl font-semibold lg:w-[95%]">
              Welcome to
              <HighlightText text={" Fake News Detection "} />, where innovation meets
              collaboration to redefine the future of human-AI interaction.
              <p className="mx-auto mt-3 text-start lg:text-center text-base font-medium text-richblack-300 lg:w-[85%]">
                At Fake News Detection, we're passionate about harnessing the power of
                artificial intelligence to empower individuals and organizations
                worldwide. Our mission is to create intelligent solutions that
                simplify tasks, drive efficiency, and unlock new opportunities
                for growth and success.
              </p>
            </header>
          </div>
        </div>
      </section>
      <section>
        <div className="mx-auto flex w-11/12 max-w-maxContent flex-col justify-between gap-10 text-richblack-500">
          <div className="flex flex-col items-center gap-10 lg:flex-row justify-between">
            <div className="my-10 flex lg:w-[50%] flex-col gap-10">
              <div className="text-4xl font-semibold lg:w-[70%]">
                <HighlightText text={"Our Founding Story"} />
              </div>
              <p className="text-base font-medium text-richblack-300 lg:w-[95%]">
                Fake News Detection's founding story is one of vision and determination.
                Born from a collective desire to harness the power of AI for
                positive change, our journey began with a simple idea: to
                streamline everyday tasks through technology. Despite
                challenges, our team persevered, driven by the belief that
                humans and AI can achieve more together than they ever could
                alone.
              </p>
              <p className="text-base font-medium text-richblack-300 lg:w-[95%]">
                Today, Fake News Detection stands as a testament to our founding
                principles. From humble beginnings, we've grown into a platform
                empowering users worldwide. As we continue to innovate and
                evolve, our commitment to creativity, collaboration, and
                empowerment remains steadfast, guiding us towards a future where
                humans and AI thrive in harmony.
              </p>
            </div>
            <div className="w-[60%] lg:w-[40%]">
              <img src={AboutUs} alt="aboutus_image" />
            </div>
          </div>

          <div className="flex flex-col items-center lg:gap-10 lg:flex-row justify-between">
            {/* Our vision and mission */}
            <div className="my-5 flex lg:w-[40%] flex-col gap-10">
              <div className="text-4xl font-semibold lg:w-[70%]">
                <HighlightText text={"Our Vision"} />
              </div>
              <p className="text-base font-medium text-richblack-300 lg:w-[95%]">
                At Fake News Detection, we envision a future where seamless integration of
                artificial intelligence empowers individuals and organizations,
                simplifying tasks, driving efficiency, and unlocking new
                opportunities for growth and success through collaborative
                human-AI interaction
              </p>
            </div>
            <div className="my-5 flex lg:w-[40%] flex-col gap-10">
              <div className="text-4xl font-semibold lg:w-[70%]">
                <HighlightText text={"Our Mission"} />
              </div>
              <p className="text-base font-medium text-richblack-300 lg:w-[95%]">
                Fake News Detection's mission is to redefine productivity through
                AI-driven solutions, empowering users to streamline tasks,
                optimize efficiency, and unlock untapped potential. By fostering
                seamless collaboration between humans and technology, we strive
                to pioneer a new era of productivity and progress in an
                ever-evolving digital landscape.
              </p>
            </div>
          </div>
        </div>
      </section>
      <section className="mx-auto my-20 flex w-11/12 max-w-maxContent flex-col justify-between gap-10 text-white">
        <ContactFormSection />
      </section>
      <Footer />
    </div>
  );
};

export default About;
