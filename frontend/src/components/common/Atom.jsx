import Adobe from "../../assets/Images/adobe.png";
import Amazon from "../../assets/Images/amazon.png";
import Apple from "../../assets/Images/apple.png";
import Flipkart from "../../assets/Images/flipkart.png";
import Google from "../../assets/Images/google.png";
import Linkedin from "../../assets/Images/linkedin.png";
import Meta from "../../assets/Images/meta.png";
import Microsoft from "../../assets/Images/microsoft.png";
import Netflix from "../../assets/Images/netflix.png";
import Ola from "../../assets/Images/ola.png";
import "./Atom.css";

const Atom = () => {
  return (
    <div className="w-full md:w-1/2">
      {/* Desktop View */}
      <div className="hidden rounded-full h-[400px] w-[400px] border-2 border-blue-100 sm:flex justify-center items-center outer-spin-animation relative mx-auto">
        <div className="bg-white absolute right-1/2 translate-x-1/2 -top-6 rounded-full p-2">
          <img src={Adobe} alt="adobe" width="30px" className="logo" />
        </div>

        <div className="bg-white absolute right-3 top-16 rounded-full p-2">
          <img src={Amazon} alt="amazon" width="30px" className="logo" />
        </div>

        <div className="bg-white absolute left-3 top-16 rounded-full p-2">
          <img src={Flipkart} alt="flipkart" width="35px" className="logo" />
        </div>

        <img
          src={Linkedin}
          alt="linkedin"
          width="45px"
          className="absolute left-40 -bottom-6 logo"
        />

        <div className="bg-white absolute left-2 bottom-16 rounded-full p-2">
          <img src={Microsoft} alt="microsoft" width="30px" className="logo" />
        </div>

        <div className="bg-white absolute right-1 bottom-16 rounded-full">
          <img src={Ola} alt="ola" width="50px" className="logo" />
        </div>

        <div className="bg-blue-100 w-[300px] h-[300px] rounded-full flex justify-center items-center">
          <div className="bg-richblack-800 w-[150px] h-[150px] rounded-full relative inner-spin-animation">
            <div className="bg-white absolute top-0 left-2 rounded-full w-[35px] h-[35px] flex justify-center items-center">
              <img src={Meta} alt="meta" width="35px" className="inner_logo" />
            </div>

            <div className="bg-white absolute top-0 right-2 rounded-full w-[35px] h-[35px] flex justify-center items-center">
              <img
                src={Apple}
                alt="apple"
                width="25px"
                className="inner_logo"
              />
            </div>

            <div className="bg-white absolute left-1 bottom-2 rounded-full p-1">
              <img
                src={Netflix}
                alt="netflix"
                width="25px"
                className="inner_logo"
              />
            </div>

            <div className="bg-white absolute bottom-2 right-0 rounded-full p-1">
              <img
                src={Google}
                alt="google"
                width="25px"
                className="inner_logo"
              />
            </div>
          </div>
        </div>
      </div>

      {/* Mobile View */}
      <div className="sm:hidden rounded-full h-[300px] w-[300px] border-2 border-blue-100 flex justify-center items-center outer-spin-animation relative mx-auto">
        <div className="bg-white absolute right-1/2 translate-x-1/2 -top-6 rounded-full p-2">
          <img src={Adobe} alt="adobe" width="25px" className="logo" />
        </div>

        <div className="bg-white absolute right-0 top-12 rounded-full p-2">
          <img src={Amazon} alt="amazon" width="25px" className="logo" />
        </div>

        <div className="bg-white absolute left-1 top-12 rounded-full p-2">
          <img src={Flipkart} alt="flipkart" width="30px" className="logo" />
        </div>

        <img
          src={Linkedin}
          alt="linkedin"
          width="40px"
          className="absolute right-1/2 translate-x-1/2 -bottom-5 logo"
        />

        <div className="bg-white absolute left-0 bottom-12 rounded-full p-2">
          <img src={Microsoft} alt="microsoft" width="25px" className="logo" />
        </div>

        <div className="bg-white absolute right-0 bottom-12 rounded-full">
          <img src={Ola} alt="ola" width="45px" className="logo" />
        </div>

        <div className="bg-blue-100 w-[200px] h-[200px] rounded-full flex justify-center items-center">
          <div className="bg-richblack-800 w-[100px] h-[100px] rounded-full relative inner-spin-animation">
            <div className="bg-white absolute bottom-0 right-1/2 translate-y-1/2 translate-x-1/2 rounded-full w-[30px] h-[30px] flex justify-center items-center">
              <img src={Meta} alt="meta" width="30px" className="inner_logo" />
            </div>

            <div className="bg-white absolute top-0 right-1/2 translate-x-1/2 -translate-y-1/2 rounded-full w-[30px] h-[30px] flex justify-center items-center">
              <img
                src={Apple}
                alt="apple"
                width="20px"
                className="inner_logo"
              />
            </div>

            <div className="bg-white absolute left-0 -translate-x-1/2 -translate-y-1/2 top-1/2 rounded-full p-1">
              <img
                src={Netflix}
                alt="netflix"
                width="20px"
                className="inner_logo"
              />
            </div>

            <div className="bg-white absolute right-0 translate-x-1/2 -translate-y-1/2 top-1/2 rounded-full p-1">
              <img
                src={Google}
                alt="google"
                width="20px"
                className="inner_logo"
              />
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Atom;
