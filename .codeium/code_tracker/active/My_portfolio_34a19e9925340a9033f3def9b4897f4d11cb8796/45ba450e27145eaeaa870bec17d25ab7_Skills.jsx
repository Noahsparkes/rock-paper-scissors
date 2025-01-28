
T/Users/noah/Personal project 23'/My_portfolio/My_portfolio/src/components/Skills.jsxÂimport { Code, Server, GitBranch, Database, Blocks, Cpu } from 'lucide-react';

const Skills = () => {
  const skillCategories = [
    {
      title: "Frontend",
      icon: <Code size={24} />,
      skills: ["React", "JavaScript", "TypeScript", "HTML5", "CSS3", "Tailwind","Next.js"]
    },
    {
      title: "Backend",
      icon: <Server size={24} />,
      skills: ["Node.js", "Express", "Python", "RESTful APIs"]
    },
    {
      title: "DevOps (in progress)",
      icon: <GitBranch size={24} />,
      skills: ["Git", "Docker", "CI/CD", "AWS", "Linux","Ansible","Jenkins","GitOps","Kubernetes"]
    },
    {
      title: "Database(in progress)",
      icon: <Database size={24} />,
      skills: ["MongoDB", "PostgreSQL", "MySQL"]
    }
  ];

  return (
    <section className="py-16 bg-white dark:bg-gray-800">
      <div className="max-w-6xl mx-auto px-4">
        <h2 className="text-3xl font-bold text-center mb-12 dark:text-white ">Technical Skills</h2>
        
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          {skillCategories.map((category) => (
            <div key={category.title} className="bg-gray-50 rounded-xl p-6 dark:bg-gray-900">
              <div className="flex items-center gap-3 mb-4">
                <div className="text-blue-600">
                  {category.icon}
                </div>
                <h3 className="text-xl font-semibold dark:text-white">{category.title}</h3>
              </div>
              
              <div className="flex flex-wrap gap-2">
                {category.skills.map((skill) => (
                  <span
                    key={skill}
                    className="px-4 py-2 bg-white rounded-lg text-sm font-medium text-gray-700 hover:bg-blue-50 hover:text-blue-600 transition-colors cursor-none"
                  >
                    {skill}
                  </span>
                ))}
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Skills;∞ 
∞± 
±Å 
ÅÖ 
ÖÂ "(34a19e9925340a9033f3def9b4897f4d11cb8796*-/Users/noah/Personal project 23'/My_portfolio2afile:///Users/noah/Personal%20project%2023%27/My_portfolio/My_portfolio/src/components/Skills.jsx::file:///Users/noah/Personal%20project%2023%27/My_portfolio