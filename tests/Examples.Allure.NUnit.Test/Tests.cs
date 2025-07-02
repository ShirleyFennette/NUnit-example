using NUnit.Allure.Core;
using NUnit.Framework;

namespace Examples.Allure.NUnit.Test
{
    [AllureNUnit]
    [Ignore]
    class Tests
    {
        [Test]
        public void Test1()
        {
            Assert.Pass();
        }
    }
}
