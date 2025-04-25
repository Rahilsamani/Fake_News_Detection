import signupImg from "../assets/Images/signup.svg";
import Template from "../components/core/Auth/Template";

function Signup() {
  return (
    <Template
      title="Embark on Your Adventure with Fake News Detection"
      description1="Discover the thrilling intersection of education and exploration on Fake News Detection, "
      description2="where learning evolves into an adventure of innovation and growth."
      image={signupImg}
      formType="signup"
    />
  );
}

export default Signup;
