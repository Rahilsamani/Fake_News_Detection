import ServiceCard from "../components/core/ServicePage/ServiceCard";
import Team1 from "../assets/Images/Khan-Tabrez-Computer-Engg.avif";
import Team2 from "../assets/Images/Mukhtar-Ansari-CO.avif";
import Team3 from "../assets/Images/Rahil.jpeg";
import Team4 from "../assets/Images/ambar.jpeg";
import Team5 from "../assets/Images/iman.jpeg";
import Team6 from "../assets/Images/aafaq.jpeg";
import Footer from "../components/common/Footer";

const Team = () => {
  const cardsData = [
    {
      heading: "Prof. Tabrez Khan",
      description: "Head of Department (Computer Engineering)",
      imageUrl: Team1,
      whereToGo: "https://www.linkedin.com/in/tabrez-khan-01982759/",
    },
    {
      heading: "Prof. Mukhtar Ansari",
      description: "Project Guide",
      imageUrl: Team2,
      whereToGo: "https://www.linkedin.com/in/mukhtar-ansari-46223121/",
    },
    {
      heading: "Iman Navdekar",
      description: "Team Lead",
      imageUrl: Team5,
      whereToGo: "https://www.linkedin.com/in/imannavdekar/",
    },
    {
      heading: "Mohammed Ambar Qadri",
      description: "Team Member",
      imageUrl: Team4,
      whereToGo: "https://www.linkedin.com/in/mohammed-ambar-qadri/",
    },
    {
      heading: "Rahil Ahmed Samani",
      description: "Team Member",
      imageUrl: Team3,
      whereToGo: "https://www.linkedin.com/in/rahil-ahmed-samani/",
    },
    {
      heading: "Aafaq Sayed",
      description: "Team Member",
      imageUrl: Team6,
      whereToGo: "https://www.linkedin.com/in/aafaq-sayed-17a047236/",
    },
  ];

  return (
    <div className="bg-richblack-800">
      <section className="relative pb-32">
        <div className="max-w-[1080px] w-11/12 mx-auto relative pt-4 mt-8">
          <h2 className="text-white text-3xl font-bold mb-10 text-center">
            Our Team
          </h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 w-full gap-x-4 gap-y-10 z-[100] relative">
            {cardsData.map((card, index) => (
              <ServiceCard
                key={index}
                heading={card.heading}
                description={card.description}
                imageUrl={card.imageUrl}
                whereToGo={card.whereToGo}
              />
            ))}
          </div>
        </div>
      </section>
      <Footer />
    </div>
  );
};

export default Team;
