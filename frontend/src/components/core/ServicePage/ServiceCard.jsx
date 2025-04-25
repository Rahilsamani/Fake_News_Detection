import { FaArrowRight } from "react-icons/fa";
import { Link } from "react-router-dom";

const ServiceCard = ({ heading, description, imageUrl, whereToGo }) => {
  return (
    <div className="bg-blue-100 bgcard1 w-full max-h-[800px] cursor-pointer p-10 bg-no-repeat transition-all duration-200 hover:scale-105 z-50">
      <div className="h-[200px] w-full flex justify-center items-center">
        <img
          src={imageUrl}
          alt={imageUrl}
          className="bg-lightBlue rounded-full h-full"
        />
      </div>
      <h3 className="font-inherit text-center text-lg font-bold pt-4">
        {heading}
      </h3>
      <p className="font-inherit text-center py-3 text-grayText leading-normal">
        {description}
      </p>
      {/* <!-- hyperlink --> */}
      <Link
        to={whereToGo}
        target="_blank"
        className="flex items-center justify-center flex-row cursor-pointer group"
      >
        <div className="font-inherit font-bold text-lightBlue500 group-hover:text-lightBlue transition-all duration-300 flex justify-center items-center gap-1 hover:text-richblack-400 bg-white px-3 py-1 rounded-lg">
          <p>Know More</p>
          <FaArrowRight
            size={13}
            className="group-hover:translate-x-1 transition-transform duration-300"
          />
        </div>
      </Link>
    </div>
  );
};

export default ServiceCard;
