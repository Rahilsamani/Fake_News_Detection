import loginImg from "../assets/Images/login.svg";
import Template from "../components/core/Auth/Template";

function Login({ setIsLoggedIn }) {
  return (
    <Template
      title="Welcome Back"
      description1="Unlock limitless potential with Fake News Detection. "
      description2="Transform your learning journey and future-proof your career."
      image={loginImg}
      formtype="login"
    />
  );
}

export default Login;
